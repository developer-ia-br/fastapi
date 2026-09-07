## Endpoint String

### Para Github
Crie um PR draft,com nome de soma string, com base na branch main

### Requirement: String
The system SHALL provide an endpoint that accepts an string value and returns that value concat with X as JSON.


#### Scenario: Valid String
- **WHEN** a client sends `GET /str/{value}` with a valid String `value`
- **THEN** the system responds with `200 OK` and a JSON body `{"result": value + 'X'}`

#### Scenario: Non-integer value is rejected
- **WHEN** a client sends `GET /str/{value}` with a `value` that is not a valid String
- **THEN** the system responds with `422 Unprocessable Entity`
