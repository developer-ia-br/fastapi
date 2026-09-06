# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

Windows venv paths are used below (`venv\Scripts\...`); adjust for `venv/bin/...` on POSIX shells.

```powershell
# Install dependencies
.\venv\Scripts\pip.exe install -r requirements.txt

# Run the dev server (auto-reload)
.\venv\Scripts\python.exe -m uvicorn app.main:app --reload

# Run the full test suite
.\venv\Scripts\python.exe -m pytest -q

# Run a single test
.\venv\Scripts\python.exe -m pytest tests/test_routes.py::test_get_item_not_found
```

## Architecture

FastAPI app using a small layered structure:

- `app/main.py` — creates the `FastAPI` app instance from `Settings` and mounts the API router. This is the ASGI entrypoint referenced as `app.main:app`.
- `app/core/config.py` — `Settings` (pydantic-settings), loaded via the cached `get_settings()`. Env vars are prefixed `APP_` (e.g. `APP_DEBUG=true`) and optionally read from a `.env` file.
- `app/api/routes.py` — a single `APIRouter` with all endpoints. As routes grow, split into multiple routers per resource and include them in `app/main.py`.
- `app/schemas/` — Pydantic models used as request/response schemas (e.g. `Item`).

Tests (`tests/`) use FastAPI's `TestClient` against the `app` instance directly (no running server needed).

There is currently no persistence layer — `app/api/routes.py` holds data in an in-memory dict as a placeholder.
