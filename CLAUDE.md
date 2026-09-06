# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

Windows venv paths are used below (`venv\Scripts\...`); adjust for `venv/bin/...` on POSIX shells.

```powershell
# Install dependencies
.\venv\Scripts\pip.exe install -r requirements.txt

# Run the dev server (auto-reload)
.\venv\Scripts\fastapi.exe dev

# Run in production mode
.\venv\Scripts\fastapi.exe run

# Run the full test suite
.\venv\Scripts\python.exe -m pytest -q

# Run a single test
.\venv\Scripts\python.exe -m pytest tests/test_routes.py::test_get_item_not_found
```

The `fastapi` CLI (from the `fastapi[standard]` extra) resolves the app via the `[tool.fastapi]` entrypoint in `pyproject.toml` (`app.main:app`), so it doesn't need a path argument.

## Architecture

FastAPI app using a small layered structure:

- `app/main.py` — creates the `FastAPI` app instance from `Settings` and includes the API routers. This is the ASGI entrypoint referenced as `app.main:app`.
- `app/core/config.py` — `Settings` (pydantic-settings), loaded via the cached `get_settings()`. Env vars are prefixed `APP_` (e.g. `APP_DEBUG=true`) and optionally read from a `.env` file.
- `app/api/` — one `APIRouter` per resource, each declaring its own `prefix`/`tags` (e.g. `app/api/health.py`, `app/api/items.py`). New resources should follow this pattern and be included in `app/main.py`.
- `app/schemas/` — Pydantic models used as request/response schemas (e.g. `Item`).

Tests (`tests/`) use FastAPI's `TestClient` against the `app` instance directly (no running server needed).

There is currently no persistence layer — `app/api/items.py` holds data in an in-memory dict as a placeholder.

## Conventions

This project follows the `fastapi` skill (`.claude/skills/fastapi/SKILL.md`): prefer return-type annotations over `response_model` (use `response_model` only when the public schema differs from the returned value), use `Annotated[..., Path()/Query()/Depends()]` for parameter and dependency declarations, declare router-level `prefix`/`tags`/shared dependencies on the `APIRouter` itself, and avoid `Ellipsis` defaults or Pydantic `RootModel`.
