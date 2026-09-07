## Purpose

Provides simple numeric utility operations over the API, starting with doubling an integer value.

## Requirements

### Requirement: Double an integer
The system SHALL provide an endpoint that accepts an integer value and returns that value multiplied by 2 as JSON.

#### Scenario: Valid integer is doubled
- **WHEN** a client sends `GET /math/double/{value}` with a valid integer `value`
- **THEN** the system responds with `200 OK` and a JSON body `{"result": value * 2}`

#### Scenario: Non-integer value is rejected
- **WHEN** a client sends `GET /math/double/{value}` with a `value` that is not a valid integer
- **THEN** the system responds with `422 Unprocessable Entity`
