#!/usr/bin/env python3
"""Build the Claude Desktop bundle (dist/garmin-mcp.mcpb) from the committed tree.

Stages HEAD's packaging files with `git archive` (so local edits, caches and
untracked files can't leak in), lifts mcpb/manifest.json and
mcpb/.python-version to the bundle root, checks that the versions agree and
uv.lock is current, packs with the CLI pinned in mcpb/package-lock.json, then
checks the bundle holds exactly the staged files, byte for byte.

Usage: python3 scripts/build_mcpb.py [--expect-version X.Y.Z] [--allow-dirty]
Standard library only; needs git, uv and Node.js (npm) on PATH.
"""

import argparse
import hashlib
import io
import json
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MCPB_DIR = REPO_ROOT / "mcpb"
OUTPUT = REPO_ROOT / "dist" / "garmin-mcp.mcpb"
PROJECT_NAME = "garmin-mcp"

# Keep in sync with the allowlist in .dockerignore (the image ships the same
# files, minus the two bundle-only ones from mcpb/).
ROOT_FILES = ["pyproject.toml", "uv.lock", "README.md", "LICENSE"]
SOURCE_DIR = "src"
BUNDLE_FILES = ["manifest.json", ".python-version"]


def run(*args: str, **kwargs) -> subprocess.CompletedProcess:
    return subprocess.run(args, check=True, **kwargs)


def git(*args: str) -> bytes:
    return run("git", "-C", str(REPO_ROOT), *args, stdout=subprocess.PIPE).stdout


def fail(message: str) -> None:
    sys.exit(f"error: {message}")


def ensure_clean_tree(allow_dirty: bool) -> None:
    status = git("status", "--porcelain").decode()
    if not status:
        return
    if not allow_dirty:
        fail(f"the working tree has changes; the bundle is built from HEAD, so commit them first "
             f"or pass --allow-dirty:\n{status}")
    print("warning: building HEAD; uncommitted changes are not in the bundle", file=sys.stderr)


def stage_tree(stage: Path) -> None:
    paths = ROOT_FILES + [SOURCE_DIR] + [f"mcpb/{name}" for name in BUNDLE_FILES]
    archive = git("archive", "--format=tar", "HEAD", "--", *paths)
    with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
        for member in tar:
            if member.issym() or member.islnk():
                fail(f"refusing to bundle link {member.name}")
            if not member.isfile():
                continue
            name = member.name
            if name.startswith("mcpb/"):
                name = name[len("mcpb/"):]
            target = stage / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(tar.extractfile(member).read())


def project_version(stage: Path) -> str:
    # tomllib needs Python 3.11; both files are machine-written, so a regex is enough.
    pyproject = (stage / "pyproject.toml").read_text(encoding="utf-8")
    table = re.search(r"^\[project\]\n(.*?)(?=^\[|\Z)", pyproject, re.M | re.S)
    match = table and re.search(r'^version\s*=\s*"([^"]+)"', table.group(1), re.M)
    if not match:
        fail("no [project] version in pyproject.toml")
    return match.group(1)


def locked_version(stage: Path) -> str:
    lock = (stage / "uv.lock").read_text(encoding="utf-8")
    versions = re.findall(rf'^\[\[package\]\]\nname = "{PROJECT_NAME}"\nversion = "([^"]+)"', lock, re.M)
    if len(versions) != 1:
        fail(f"expected one {PROJECT_NAME} package in uv.lock, found {len(versions)}")
    return versions[0]


def check_stage(stage: Path, expect_version: str) -> dict:
    manifest = json.loads((stage / "manifest.json").read_text(encoding="utf-8"))
    entry_point = stage / manifest["server"]["entry_point"]
    if not entry_point.is_file():
        fail(f"entry_point {manifest['server']['entry_point']} is not in the bundle")

    versions = {
        "mcpb/manifest.json": manifest["version"],
        "pyproject.toml": project_version(stage),
        "uv.lock": locked_version(stage),
    }
    if expect_version:
        versions["--expect-version"] = expect_version
    if len(set(versions.values())) != 1:
        fail(f"versions disagree: {versions}")

    # `uv run --frozen` trusts the bundled lock as is, so a stale one would only
    # show up as a missing module on the user's machine. Not --offline: uv needs
    # the .python-version interpreter here and may have to download it.
    run("uv", "lock", "--check", "--directory", str(stage))
    return manifest


def mcpb_cli() -> Path:
    package = MCPB_DIR / "node_modules" / "@anthropic-ai" / "mcpb"
    locked = json.loads((MCPB_DIR / "package-lock.json").read_text())
    wanted = locked["packages"]["node_modules/@anthropic-ai/mcpb"]["version"]
    installed = package / "package.json"
    if not installed.is_file() or json.loads(installed.read_text())["version"] != wanted:
        npm = shutil.which("npm")
        if not npm:
            fail("npm not found on PATH")
        run(npm, "ci", "--ignore-scripts", "--no-audit", "--no-fund", "--prefix", str(MCPB_DIR))
    return package / json.loads(installed.read_text())["bin"]


def check_bundle(stage: Path, expected: set) -> None:
    with zipfile.ZipFile(OUTPUT) as bundle:
        names = bundle.namelist()
        if sorted(names) != sorted(expected):
            fail(f"bundle contents differ from the allowlist: "
                 f"extra {sorted(set(names) - expected)}, missing {sorted(expected - set(names))}")
        for name in names:
            if bundle.read(name) != (stage / name).read_bytes():
                fail(f"{name} in the bundle differs from the staged copy")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--expect-version", default="", help="fail unless the bundle has this version")
    parser.add_argument("--allow-dirty", action="store_true", help="build HEAD even if the tree has changes")
    args = parser.parse_args()

    ensure_clean_tree(args.allow_dirty)
    with tempfile.TemporaryDirectory() as tmp:
        stage = Path(tmp) / PROJECT_NAME
        stage.mkdir()
        stage_tree(stage)
        manifest = check_stage(stage, args.expect_version)

        sources = git("ls-tree", "-r", "-z", "--name-only", "HEAD", "--", SOURCE_DIR).decode().split("\0")
        expected = set(ROOT_FILES + BUNDLE_FILES + [path for path in sources if path])

        OUTPUT.parent.mkdir(exist_ok=True)
        OUTPUT.unlink(missing_ok=True)
        run("node", str(mcpb_cli()), "pack", str(stage), str(OUTPUT))
        check_bundle(stage, expected)

    digest = hashlib.sha256(OUTPUT.read_bytes()).hexdigest()
    print(f"Built {OUTPUT.relative_to(REPO_ROOT)}: version {manifest['version']}, "
          f"{len(expected)} files, sha256 {digest}")


if __name__ == "__main__":
    main()
