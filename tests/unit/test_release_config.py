"""Release metadata regression tests.

release-please bumps the version in pyproject.toml and, through
``extra-files`` entries, in uv.lock, the MCP Bundle manifest and the
README's pinned auth command. If uv.lock drifts, ``uv lock --check`` and the
Docker build (``uv sync --locked``) both fail; if the bundle manifest drifts,
the release ships without a bundle. Release PRs are opened with GITHUB_TOKEN,
so no checks run on them: these tests are what guards the updater config.
"""

import json
import re
from pathlib import Path

import pytest

tomllib = pytest.importorskip("tomllib")

REPO_ROOT = Path(__file__).resolve().parents[2]


def _load_toml(name: str) -> dict:
    with open(REPO_ROOT / name, "rb") as fh:
        return tomllib.load(fh)


def _project() -> dict:
    return _load_toml("pyproject.toml")["project"]


def _release_config() -> dict:
    return json.loads((REPO_ROOT / "release-please-config.json").read_text())


def _locked_project_versions(name: str) -> list[str]:
    packages = _load_toml("uv.lock")["package"]
    return [pkg["version"] for pkg in packages if pkg["name"] == name]


def _extra_files(path: str) -> list[dict]:
    package = _release_config()["packages"]["."]
    return [f for f in package.get("extra-files", []) if f["path"] == path]


def _readme_release_blocks() -> list[str]:
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    return re.findall(r"<!-- x-release-please-start-version -->\n(.*?)<!-- x-release-please-end -->", readme, re.S)


def test_manifest_matches_pyproject_version() -> None:
    manifest = json.loads((REPO_ROOT / ".release-please-manifest.json").read_text())

    assert manifest == {".": _project()["version"]}


def test_uv_lock_matches_pyproject_version() -> None:
    project = _project()

    assert _locked_project_versions(project["name"]) == [project["version"]]


def test_mcpb_manifest_matches_pyproject_version() -> None:
    manifest = json.loads((REPO_ROOT / "mcpb" / "manifest.json").read_text(encoding="utf-8"))

    assert manifest["version"] == _project()["version"]


def test_readme_auth_command_pins_the_current_release() -> None:
    blocks = _readme_release_blocks()

    assert blocks, "README.md has no x-release-please-start-version block"
    for block in blocks:
        # The generic updater rewrites every X.Y.Z inside the block, so nothing
        # else that looks like a version may live there.
        assert re.findall(r"\d+\.\d+\.\d+", block) == [_project()["version"]], block
    assert any(f"/archive/refs/tags/{_project()['version']}.tar.gz" in block for block in blocks)


def test_release_please_bumps_uv_lock_entry_for_this_project() -> None:
    lock_updaters = _extra_files("uv.lock")

    assert len(lock_updaters) == 1
    updater = lock_updaters[0]
    assert updater["type"] == "toml"
    # release-please's TOML parser wraps strings as {start, end, value}, so the
    # filter has to compare ``name.value``; a plain ``@.name == ...`` matches nothing.
    match = re.fullmatch(r"\$\.package\[\?\(@\.name\.value=='([^']+)'\)\]\.version", updater["jsonpath"])
    assert match, updater["jsonpath"]
    assert match.group(1) == _project()["name"]


def test_release_please_bumps_mcpb_manifest_version() -> None:
    # GenericJson only logs a warning when the jsonpath matches nothing, and the
    # bundle build then fails on the tagged commit after the release is out.
    assert _extra_files("mcpb/manifest.json") == [
        {"type": "json", "path": "mcpb/manifest.json", "jsonpath": "$.version"}
    ]


def test_release_please_bumps_readme_auth_command() -> None:
    assert _extra_files("README.md") == [{"type": "generic", "path": "README.md"}]


def test_release_tags_continue_the_existing_unprefixed_scheme() -> None:
    config = _release_config()

    # The repo's first tag is ``0.1.0`` (no ``v``); release-please finds the
    # previous release by tag name, so the format has to match.
    assert config["release-type"] == "python"
    assert config["include-v-in-tag"] is False
    assert config["include-component-in-tag"] is False
