# GitHub Actions Workflows

This repository uses GitHub Actions for continuous integration and security checks. Below is an overview of each workflow.

## Workflows

### 1. CI (`ci.yml`)

**Triggers:**
- Pull requests to `main` or `master`
- Pushes to `main` or `master`

**What it does:**
- Tests the codebase across Python versions 3.10, 3.11, 3.12, and 3.13
- Runs all integration and unit tests
- Uses uv for fast dependency management
- Provides a test summary

**Matrix:** Tests run in parallel across 4 Python versions for comprehensive compatibility checks.

### 2. PR Validation (`pr-validation.yml`)

**Triggers:**
- Pull request opened, synchronized, or reopened

**What it does:**
- Comprehensive validation on Python 3.13
- Runs all tests with strict markers and fail-fast behavior (max 5 failures)
- Validates package installation
- Checks `pyproject.toml` syntax
- Provides PR metadata information

**Jobs:**
1. `validate` - Runs complete test suite
2. `test-installation` - Verifies the package installs correctly
3. `pr-info` - Displays PR metadata for debugging

### 3. Security Checks (`security.yml`)

**Triggers:**
- Pull requests to `main` or `master`
- Weekly schedule (Mondays at 9am UTC)
- Manual trigger via workflow_dispatch

**What it does:**
- Checks dependency vulnerabilities
- Verifies lock file (`uv.lock`) is in sync with `pyproject.toml`
- Validates Python syntax across all source files
- Checks package import structure

**Jobs:**
1. `dependency-check` - Security and dependency validation
2. `code-quality` - Code syntax and import checks

### 4. Release (`release.yml`)

**Triggers:**
- Pushes to `main`
- Pull requests to `main` or `master` (build and smoke test only, nothing is pushed)
- Manual trigger via workflow_dispatch, to republish the image of an existing release tag (and attach its bundle if missing)

**What it does:**
- [release-please](https://github.com/googleapis/release-please) keeps a release PR open with the next version and changelog, computed from [Conventional Commits](https://www.conventionalcommits.org/) (`fix:` bumps the patch version, `feat:` the minor version; while the version is `0.x`, breaking changes also bump the minor version). Merging that PR bumps `pyproject.toml`, `uv.lock`, `mcpb/manifest.json` and the pinned auth command in `README.md`, tags the release (`X.Y.Z`, no `v` prefix) and creates the GitHub release.
- Builds the Docker image natively on `amd64` and `arm64` runners and runs `scripts/docker_smoke_test.py` against each: MCP `initialize` + `tools/list` over streamable-http and stdio, plus the image `HEALTHCHECK`. No Garmin credentials are needed. The build itself fails if `uv.lock` is out of date (`uv sync --locked`).
- Pushes both architectures to `ghcr.io/<owner>/garmin_mcp` and merges them into one multi-arch tag set: `main` and `sha-<commit>` on every push, plus `X.Y.Z`, `X.Y` and `latest` when a release is created (built from the tagged commit). `latest` never points at an unreleased build, and the rolling tags only move forward: `latest` follows the newest release and `X.Y` the newest patch of `X.Y`.
- Publishes SBOM and provenance attestations with the image, plus a signed build provenance attestation (`gh attestation verify`).
- For a release, calls `mcpb.yml` to build, test and attach the Claude Desktop bundle. The bundle and the image only share `meta`; neither waits for the other.

Publishing runs in this workflow rather than on `release: published` because releases created with `GITHUB_TOKEN` don't trigger other workflows.

**Jobs:**
1. `release-please` - Release PR, tag and GitHub release (pushes only)
2. `meta` - Commit to build, image name and tags
3. `build` - Per-architecture build, smoke test and push by digest
4. `publish` - Multi-arch tags and attestation (not on pull requests)
5. `mcpb` - Calls `mcpb.yml` with `publish: true` (releases only)

**One-time setup:**
- Settings → Actions → General → Workflow permissions: enable *Allow GitHub Actions to create and approve pull requests* (release-please opens the release PR).
- After the first push, the GHCR package is private: Package settings → Change visibility → Public, so `docker pull` works without logging in.
- Keep *immutable releases* off (Settings → General → Releases): the bundle is attached after release-please has published the release, which an immutable release no longer allows.

**Cutting a release:** merge the open `chore(main): release X.Y.Z` PR. Because `GITHUB_TOKEN` opened it, pull request checks don't run on that PR on their own; it only changes version numbers and the changelog, and the image is still smoke-tested after the merge.

**If a release has no image** (the run failed or was cancelled after the tag was created): Actions → Release → Run workflow, with the release tag as `version`. Republishing an older release only updates its own `X.Y.Z` tag (and `X.Y` if it is still the newest patch of that minor version); `latest` stays on the newest release.

**If a release has no bundle:** open the failed run and use *Re-run failed jobs*. It reuses the run's release outputs and doesn't touch the image. If that run is gone, the manual run above also attaches the bundle when the release lacks it, but it republishes the image as well. Set `replace_assets` only to replace a bundle that is already attached: packing isn't byte-reproducible, so the replacement gets a new digest.

### 5. MCP Bundle (`mcpb.yml`)

**Triggers:**
- Pull requests to `main` or `master`
- Called by `release.yml` for each release (`workflow_call`)

**What it does:**
- `pack` runs `scripts/build_mcpb.py`: it stages the committed packaging files (`pyproject.toml`, `uv.lock`, `README.md`, `LICENSE`, `src/`, plus `mcpb/manifest.json` and `mcpb/.python-version` at the bundle root), checks that the manifest, `pyproject.toml`, `uv.lock` and the release version agree and that `uv.lock` is current, packs with the mcpb CLI pinned in `mcpb/package-lock.json`, and checks the bundle holds exactly those files, byte for byte. The bundle is uploaded as a plain `garmin-mcp.mcpb` run artifact (kept 7 days) that opens directly in Claude Desktop. Commits without `mcpb/manifest.json` (releases from before the bundle) are skipped with a notice.
- `smoke` runs `scripts/mcpb_smoke_test.py` on Linux, macOS and Windows, each with the pinned uv and with uv 0.9.7 (the uv Claude Desktop downloads when none is installed). It installs the bundle like Desktop does (`uv sync`, Python 3.12 from `.python-version`), starts it cold and warm from the manifest's `mcp_config`, and checks `initialize` and that `tools/list` matches the manifest. Startup times go to the job summary. No Garmin credentials are needed.
- `attach` (releases only) checks the artifact's sha256 against `pack`, publishes a signed build provenance attestation and uploads `garmin-mcp.mcpb` to the release. It skips with a notice if the release already has the file, unless `replace_assets` is set.

To move to immutable releases later, release-please would have to create draft releases (`draft: true` with `force-tag-creation`), and `attach` would publish them (`gh release edit --draft=false`) after uploading.

### 6. Dependabot (`dependabot.yml`)

Workflows pin actions to commit SHAs, the Dockerfile pins `uv`, and `mcpb/package-lock.json` pins the mcpb CLI. Dependabot opens a weekly PR for each to keep those pins current (actions are grouped into one). The uv versions in `mcpb.yml` are not covered; keep them in step with the Dockerfile.

## Running Tests Locally

To run the same tests that CI runs:

```bash
# Install dependencies
uv sync

# Run integration and unit tests
uv run pytest tests/integration tests/unit -v --tb=short

# Check lock file status
uv lock --check

# Build the image and run the Docker smoke test
docker build -t garmin-mcp:local .
python3 scripts/docker_smoke_test.py garmin-mcp:local

# Build the Claude Desktop bundle from HEAD and smoke-test it (needs Node.js 18+; CI uses 22)
python3 scripts/build_mcpb.py
python3 scripts/mcpb_smoke_test.py dist/garmin-mcp.mcpb

# After changing tools, refresh the bundle manifest's tools list
uv run python scripts/generate_mcpb_tools.py
```

## Skipped Tests

The workflows skip end-to-end (e2e) tests because they require valid Garmin credentials. E2E tests are located in `tests/e2e/` and should be run manually with proper authentication.

## Badge Status

Add these badges to your README.md:

```markdown
![CI](https://github.com/YOUR_USERNAME/garmin_mcp/workflows/CI/badge.svg)
![PR Validation](https://github.com/YOUR_USERNAME/garmin_mcp/workflows/PR%20Validation/badge.svg)
![Security Checks](https://github.com/YOUR_USERNAME/garmin_mcp/workflows/Security%20Checks/badge.svg)
```

## Troubleshooting

### Lock file out of sync

If the security check fails with "Lock file is out of sync":

```bash
uv lock
git add uv.lock
git commit -m "Update uv.lock"
```

### Test failures

Check the Actions tab for detailed test output. Tests run with `-v --tb=short` for verbose output with short tracebacks.
