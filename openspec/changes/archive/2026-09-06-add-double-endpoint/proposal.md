## Why

The API currently exposes only `health` and `items` resources. There is no endpoint for simple numeric operations, and a client needs a way to double an integer via the API.

## What Changes

- Add a new `math` router (`app/api/math.py`) with a `GET /math/double/{value}` endpoint.
- The endpoint accepts an integer path parameter, multiplies it by 2, and returns the result as JSON.
- Register the new router in `app/main.py`.

## Capabilities

### New Capabilities
- `math`: numeric utility operations exposed over the API, starting with doubling an integer.

### Modified Capabilities
(none)

## Impact

- New file: `app/api/math.py` (router) and its response schema.
- Modified: `app/main.py` (include the new router).
- New tests covering the endpoint in `tests/`.
- No changes to existing `items` or `health` behavior.
