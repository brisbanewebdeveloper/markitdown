## 2026-03-29

- Added local MCP HTTP runtime helpers with `docker-compose.yml` and `restart.sh` for running `markitdown-mcp` on port 3001, with env-configurable port and workdir settings plus UID/GID passthrough for mounted files.
- Updated `packages/markitdown-mcp/README.md` to document HTTP client setup via `mcp-config.json` and cleaned related command block formatting.
- Added `.history` to `.gitignore` to avoid committing editor history artifacts.
- Added `.github/copilot-instructions.md` with branch-specific workflow notes to keep patches minimal and require `UPDATES.md` maintenance on the `custom` branch.
