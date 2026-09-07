# ci-pipeline Specification

## Purpose

Garante que todo pull request contra `main` seja automaticamente validado (testes e lint) antes de ser mesclado, e libera o merge automaticamente quando essas validações passam.

## Requirements

### Requirement: Validação automática de pull requests
The system SHALL run the automated test suite and a lint/format check on every pull request targeting `main`, on creation and on every subsequent push to that pull request.

#### Scenario: Pull request aberto ou atualizado
- **WHEN** a pull request targeting `main` is opened or receives a new push
- **THEN** the system runs the test suite and the lint/format check and reports their result as a check on the pull request

### Requirement: Bloqueio de merge em caso de falha
The system SHALL prevent a pull request from being merged while any required validation (tests or lint/format) is failing.

#### Scenario: Testes ou lint falham
- **WHEN** the test suite or the lint/format check fails for a pull request
- **THEN** the pull request's check reports failure and the pull request is not merged automatically

### Requirement: Auto-merge condicional
The system SHALL automatically merge a pull request targeting `main` once all required validations succeed, without requiring manual merge action.

#### Scenario: Todas as validações passam
- **WHEN** the test suite and the lint/format check both succeed for a pull request targeting `main`
- **THEN** the system merges the pull request automatically

#### Scenario: Deploy fora de escopo
- **WHEN** a pull request is automatically merged
- **THEN** the system SHALL NOT trigger any deployment action, since no deployment target is defined for this capability
