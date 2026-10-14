"""Regression tests for the MCP Bundle manifest."""

import asyncio
import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).parents[2]
MANIFEST_PATH = REPO_ROOT / "mcpb" / "manifest.json"
sys.path.insert(0, str(REPO_ROOT / "scripts"))


def _read_manifest():
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def test_token_path_default_does_not_require_nested_interpolation():
    manifest = _read_manifest()
    assert manifest["user_config"]["token_path"]["default"] == "~/.garminconnect"


def test_user_config_defaults_do_not_contain_template_variables():
    manifest = _read_manifest()

    for config in manifest.get("user_config", {}).values():
        default = config.get("default")
        values = default if isinstance(default, list) else [default]
        assert all("${" not in value for value in values if isinstance(value, str))


def test_manifest_file_is_canonically_serialized():
    """release-please rewrites the whole file when it bumps the version; if the
    committed text isn't in the same form, every release PR churns other lines."""
    from generate_mcpb_tools import serialize_manifest

    text = MANIFEST_PATH.read_text(encoding="utf-8")
    assert text == serialize_manifest(json.loads(text)), "run scripts/generate_mcpb_tools.py"


def test_tools_list_matches_registered_tools():
    """The manifest's tools list must track the server's actual tool set (#340)."""
    from generate_mcpb_tools import _collect_tools

    manifest = _read_manifest()
    assert manifest["tools"] == asyncio.run(_collect_tools()), "run scripts/generate_mcpb_tools.py"


def test_bundle_allowlist_matches_docker_allowlist():
    """The bundle and the image ship the same project files; the bundle adds
    only its own files from mcpb/."""
    import build_mcpb

    dockerignore = (REPO_ROOT / ".dockerignore").read_text().splitlines()
    docker_files = {line[1:].rstrip("/") for line in dockerignore if line.startswith("!")}

    assert set(build_mcpb.ROOT_FILES + [build_mcpb.SOURCE_DIR]) == docker_files
    assert all((REPO_ROOT / "mcpb" / name).is_file() for name in build_mcpb.BUNDLE_FILES)
