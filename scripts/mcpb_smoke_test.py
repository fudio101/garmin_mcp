#!/usr/bin/env python3
"""Smoke-test a built garmin-mcp.mcpb the way Claude Desktop installs and runs it.

Unpacks the bundle into a path with spaces, runs `uv sync --quiet` there (what
Desktop does at install time), then starts the server from the manifest's
`mcp_config.args` with `${__dirname}` and `${user_config.*}` filled in the way
Desktop fills them, and checks it speaks MCP over stdio and lists every tool in
the manifest. The install runs with an empty uv cache and no Python installed.
The server then starts twice: cold (first launch right after the install,
unset optional fields passed as literal placeholders) and warm (second
launch, empty strings).

GARMINTOKENS points at an empty directory and no credentials are set, so the
background login gives up before contacting Garmin.

Usage: python3 scripts/mcpb_smoke_test.py dist/garmin-mcp.mcpb
Standard library only; needs uv on PATH.
"""

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import zipfile
from pathlib import Path

COLD_TIMEOUT = 180
COLD_WARN_AFTER = 45
WARM_TIMEOUT = 60
REPLY_TIMEOUT = 30

INITIALIZE_REQUEST = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
        "protocolVersion": "2025-06-18",
        "capabilities": {},
        "clientInfo": {"name": "mcpb-smoke-test", "version": "0"},
    },
}
INITIALIZED_NOTIFICATION = {"jsonrpc": "2.0", "method": "notifications/initialized"}
LIST_TOOLS_REQUEST = {"jsonrpc": "2.0", "id": 2, "method": "tools/list"}

PLACEHOLDER = re.compile(r"\$\{([^}]+)\}")


def annotate(level: str, message: str) -> None:
    if os.environ.get("GITHUB_ACTIONS") == "true":
        print(f"::{level}::{message}")
    else:
        print(f"{level}: {message}", file=sys.stderr)


def summarize(line: str) -> None:
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as fh:
            fh.write(line + "\n")


def resolve(value: str, variables: dict) -> str:
    # Like Desktop, leave placeholders it has no value for as literal text.
    return PLACEHOLDER.sub(lambda m: variables.get(m.group(1), m.group(0)), value)


def unpack(bundle: Path, root: Path) -> Path:
    extension = root / "Claude Extensions" / "local.mcpb.alexandre-domingues.garmin-mcp"
    with zipfile.ZipFile(bundle) as archive:
        archive.extractall(extension)
    return extension


def uv_sync(extension: Path, env: dict) -> float:
    lock_before = (extension / "uv.lock").read_bytes()
    started = time.monotonic()
    subprocess.run(["uv", "sync", "--quiet"], cwd=extension, env=env, check=True, timeout=COLD_TIMEOUT)
    elapsed = time.monotonic() - started
    assert (extension / "uv.lock").read_bytes() == lock_before, "uv sync rewrote the bundled uv.lock"

    pyvenv = (extension / ".venv" / "pyvenv.cfg").read_text(encoding="utf-8")
    version = re.search(r"^version_info\s*=\s*(\S+)", pyvenv, re.M)
    assert version and version.group(1).startswith("3.12."), f"venv is not Python 3.12:\n{pyvenv}"
    return elapsed


def start_server(extension: Path, manifest: dict, user_config: dict, env: dict, timeout: float) -> "tuple[float, list]":
    """Run one MCP handshake; return seconds to the initialize reply and the tool names."""
    variables = {"__dirname": str(extension)}
    variables.update({f"user_config.{key}": value for key, value in user_config.items()})
    config = manifest["server"]["mcp_config"]
    # Desktop ignores `command` for uv bundles and runs its own uv with `args`.
    args = [resolve(arg, variables) for arg in config["args"]]
    assert not any("${" in arg for arg in args), args
    env = dict(env, **{key: resolve(value, variables) for key, value in config.get("env", {}).items()})

    with tempfile.TemporaryFile(mode="w+", encoding="utf-8", errors="replace") as stderr:
        started = time.monotonic()
        proc = subprocess.Popen(
            ["uv", *args], cwd=extension, env=env, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
            stderr=stderr, text=True, encoding="utf-8",
        )
        replies: dict = {}
        stray: list = []

        def read_stdout() -> None:
            for line in proc.stdout:
                try:
                    message = json.loads(line)
                except ValueError:
                    stray.append(line)
                    continue
                if not isinstance(message, dict) or message.get("jsonrpc") != "2.0":
                    stray.append(line)
                elif "id" in message:
                    replies[message["id"]] = message

        def wait_reply(request: dict, limit: float) -> dict:
            deadline = time.monotonic() + limit
            while request["id"] not in replies:
                if proc.poll() is not None:
                    raise RuntimeError(f"server exited ({proc.returncode}) before replying to {request['method']}")
                if time.monotonic() > deadline:
                    raise TimeoutError(f"no reply to {request['method']} within {limit:.0f}s")
                time.sleep(0.1)
            return replies[request["id"]]

        reader = threading.Thread(target=read_stdout, daemon=True)
        reader.start()
        try:
            proc.stdin.write(json.dumps(INITIALIZE_REQUEST) + "\n")
            proc.stdin.flush()
            reply = wait_reply(INITIALIZE_REQUEST, timeout)
            elapsed = time.monotonic() - started
            assert "result" in reply, reply

            for message in (INITIALIZED_NOTIFICATION, LIST_TOOLS_REQUEST):
                proc.stdin.write(json.dumps(message) + "\n")
            proc.stdin.flush()
            tools = [tool["name"] for tool in wait_reply(LIST_TOOLS_REQUEST, REPLY_TIMEOUT)["result"]["tools"]]

            proc.stdin.close()
            proc.wait(timeout=30)
            reader.join(timeout=5)
            assert not stray, f"non-JSON-RPC output on stdout: {stray[:5]}"
            return elapsed, tools
        except BaseException:
            proc.kill()
            proc.wait()
            stderr.seek(0)
            sys.stderr.write(stderr.read())
            raise


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    bundle = Path(sys.argv[1]).resolve()

    root = Path(tempfile.mkdtemp(prefix="mcpb smoke "))
    try:
        extension = unpack(bundle, root)
        manifest = json.loads((extension / "manifest.json").read_text(encoding="utf-8"))
        expected_tools = sorted(tool["name"] for tool in manifest["tools"])
        tokens = root / "empty tokens"
        tokens.mkdir()

        env = dict(os.environ, UV_CACHE_DIR=str(root / "uv-cache"), UV_PYTHON_INSTALL_DIR=str(root / "uv-python"))
        # Desktop doesn't set these; UV_PYTHON (exported by setup-uv's
        # python-version) would override the bundle's .python-version.
        for name in ("UV_PYTHON", "VIRTUAL_ENV"):
            env.pop(name, None)

        uv = subprocess.run(["uv", "--version"], check=True, capture_output=True, text=True).stdout.strip()
        install = uv_sync(extension, env)
        print(f"install (uv sync): {install:.1f}s with {uv}")

        runs = [
            # Desktop passes unset optional fields through as the literal placeholder.
            ("cold", {"token_path": str(tokens)}, COLD_TIMEOUT),
            ("warm", {"token_path": str(tokens), "garmin_email": "", "garmin_password": ""}, WARM_TIMEOUT),
        ]
        timings = {}
        for name, user_config, timeout in runs:
            elapsed, tools = start_server(extension, manifest, user_config, env, timeout)
            assert sorted(tools) == expected_tools, (
                f"{name}: server lists {len(tools)} tools, manifest has {len(expected_tools)}"
            )
            timings[name] = elapsed
            print(f"{name} start: ok, initialize after {elapsed:.1f}s, {len(tools)} tools")

        # What a user waits through on first install: the sync, then the first launch.
        first_run = install + timings["cold"]
        if first_run > COLD_WARN_AFTER:
            annotate("warning", f"install and cold start took {first_run:.0f}s (over {COLD_WARN_AFTER}s)")
        summarize(
            "| Platform | uv | Install | Cold start | Warm start |\n|---|---|---|---|---|\n"
            f"| {sys.platform} | {uv} | {install:.1f}s | {timings['cold']:.1f}s | {timings['warm']:.1f}s |"
        )
    finally:
        shutil.rmtree(root, ignore_errors=True)


if __name__ == "__main__":
    main()
