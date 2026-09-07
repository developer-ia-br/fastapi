## Why

O repositório não possui nenhuma automação de CI hoje (não há diretório `.github/`, nem lint configurado). Mudanças como `add-string-endpoint` dependem de execução manual de `pytest` antes do merge, o que não escala e não impede que um PR com testes quebrados seja mesclado.

## What Changes

- Adicionar um workflow do GitHub Actions (`.github/workflows/ci.yml`) que roda em pull requests contra `main`.
- O workflow instala as dependências do projeto, roda a suíte `pytest` e roda lint/format-check com `ruff` (ferramenta ainda não usada no projeto — assumida como padrão por ser o lint mais comum no ecossistema Python/FastAPI atual; ver Impact).
- Se todas as validações passarem, o workflow habilita auto-merge do PR (via `gh pr merge --auto` ou equivalente na Action), respeitando as regras de branch protection do repositório.
- Se qualquer validação falhar, o PR permanece bloqueado para merge e o workflow reporta a falha nos checks do PR.
- Deploy **não** faz parte deste change — não há infraestrutura de deploy no repositório ainda.

## Capabilities

### New Capabilities
- `ci-pipeline`: automação de validação e merge de pull requests via GitHub Actions, cobrindo testes automatizados, lint/format e auto-merge condicional.

### Modified Capabilities
(nenhuma)

## Impact

- Novo arquivo: `.github/workflows/ci.yml`.
- Nova dependência de desenvolvimento: `ruff` (adicionada a `requirements.txt` ou a um novo `requirements-dev.txt` — decisão de organização registrada em `design.md`).
- Nenhuma alteração no comportamento runtime da API (`app/`) — este change afeta apenas o pipeline de entrega.
- Pré-requisito operacional fora do controle deste change: o repositório precisa ter uma branch protection rule em `main` exigindo o check de CI antes do merge, e permissões do `GITHUB_TOKEN` (ou de um token com escopo de merge) habilitadas para auto-merge. Isso é configuração do repositório no GitHub, não um artefato versionado — será sinalizado como passo manual em `tasks.md`.
- Assunção: "auto-merge" aqui significa habilitar o recurso nativo de auto-merge do GitHub (squash/merge quando os checks obrigatórios passarem), não um merge forçado imediato — assim o PR ainda respeita qualquer outro check obrigatório configurado no repositório.
