## 2026-03-29

- Added local MCP HTTP runtime helpers with `docker-compose.yml` and `restart.sh` for running `markitdown-mcp` on port 3001, with env-configurable port and workdir settings plus UID/GID passthrough for mounted files.
- Updated `packages/markitdown-mcp/README.md` to document HTTP client setup via `mcp-config.json` and cleaned related command block formatting.
- Added `.history` to `.gitignore` to avoid committing editor history artifacts.
- Added `.github/copilot-instructions.md` with branch-specific workflow notes to keep patches minimal and require `UPDATES.md` maintenance on the `custom` branch.

## 2026-04-22

- Replaced `packages/markitdown-mcp/src/markitdown_mcp/__main__.py` tool input handling so `convert_to_markdown` now accepts client-supplied base64 file content plus optional metadata and converts it via `MarkItDown.convert_stream(...)` instead of reading `file:` or remote URIs on the server.
- Added focused MCP tests in `packages/markitdown-mcp/tests/test_main.py` covering base64 HTML conversion, notebook conversion with filename hints, and invalid payload rejection.
- Updated `packages/markitdown-mcp/README.md` to document the new payload-based tool contract, remove outdated local-mount guidance for uploaded content, and adjust the security and inspector guidance accordingly.
- Verified the new behavior in an isolated virtual environment with `python -m pytest tests/test_main.py` from `packages/markitdown-mcp`, which passed with 4 tests.
