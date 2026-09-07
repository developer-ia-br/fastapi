## Purpose

Provê operações utilitárias simples sobre strings via API, começando pela concatenação de um sufixo fixo a um valor de texto recebido.

## ADDED Requirements

### Requirement: Concatenar sufixo a uma string
The system SHALL provide an endpoint that accepts a string value and returns that value concatenated with the fixed suffix `"X"` as JSON.

#### Scenario: Valor válido é concatenado
- **WHEN** a client sends `GET /str/{value}` with a non-empty `value`
- **THEN** the system responds with `200 OK` and a JSON body `{"result": value + "X"}`
