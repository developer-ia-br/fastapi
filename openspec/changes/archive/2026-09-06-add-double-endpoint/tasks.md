## 1. Schema

- [x] 1.1 Add a `DoubleResult` Pydantic model (`result: int`) in `app/schemas/math.py` and verify it imports cleanly

## 2. Router

- [x] 2.1 Create `app/api/math.py` with an `APIRouter(prefix="/math", tags=["math"])` exposing `GET /double/{value}` that takes an `Annotated[int, Path(...)]` value, multiplies it by 2, and returns a `DoubleResult` via the function's return-type annotation
- [x] 2.2 Register the router in `app/main.py` via `app.include_router(math_router)` and verify `GET /math/double/5` returns `{"result": 10}` when running the app locally

## 3. Tests

- [x] 3.1 Add `tests/test_routes.py` cases: a valid integer returns `200` with the doubled `result`, and a non-integer path value returns `422` — verify with `pytest -q`
