# Repository Guidelines

## Project Structure & Module Organization

- `app/main.py` creates the FastAPI application and registers routers.
- `app/api/` contains resource routers, currently health and item endpoints.
- `app/schemas/` contains Pydantic request and response models.
- `app/core/config.py` defines settings and the cached `get_settings()` accessor.
- `tests/` contains route tests using FastAPI's `TestClient`.

Item data currently lives in an in-memory dictionary in `app/api/items.py`; there is no database or frontend asset pipeline. Add new resource routers under `app/api/` and register them in `app/main.py`.

## Build, Test, and Development Commands

Run these PowerShell commands from the repository root with the existing virtual environment:

```powershell
.\venv\Scripts\pip.exe install -r requirements.txt
.\venv\Scripts\fastapi.exe dev
.\venv\Scripts\fastapi.exe run
.\venv\Scripts\python.exe -m pytest -q
.\venv\Scripts\python.exe -m pytest tests/test_routes.py::test_get_item_not_found
```

These install dependencies, start development with reload, start production mode, run all tests, and run one test, respectively. The CLI entrypoint is configured as `app.main:app` in `pyproject.toml`. No separate build step is configured.

## Coding Style & Naming Conventions

Use four-space indentation, `snake_case` for modules and functions, and `PascalCase` for models. Annotate function parameters and return values. Prefer `Annotated[..., Path()/Query()/Depends()]` and return-type response schemas. Declare router prefixes and tags on `APIRouter`. Avoid ellipsis defaults and Pydantic `RootModel`. No formatter or linter is currently configured; follow existing style.

## Testing Guidelines

Use pytest, `test_*.py` files, and `test_*` functions. Cover successful responses, missing resources, and invalid input when changing routes. Assert status codes and relevant response fields. Tests require no running server. No coverage threshold is configured.

## Commit & Pull Request Guidelines

History uses short descriptive subjects, mostly in Portuguese, without a consistent Conventional Commits prefix. Keep commits focused. PRs should explain the change, affected behavior, and test results; link relevant issues. Include request/response examples for API changes.

## Configuration & Agent Instructions

Settings load optional `.env` values with the `APP_` prefix, including `APP_DEBUG` and `APP_APP_NAME`. Keep credentials out of commits and disable debug in production.

For library, framework, SDK, API, CLI, or cloud-service documentation, use Context7: resolve the library ID first, then query one concept per call. Skip resolution only for an exact supplied library ID. Prefer authoritative, version-matched results over web search. This requirement excludes general programming, business-logic debugging, refactoring, and code review unless explicitly requested.
