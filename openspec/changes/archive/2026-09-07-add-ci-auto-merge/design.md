## Context

O repositório está hospedado no GitHub, não tem nenhum workflow em `.github/`, e não tem nenhuma ferramenta de lint/format configurada. O ambiente de desenvolvimento local usa Python 3.13 (visível no cache do pytest: `tests/__pycache__/*.cpython-313-*.pyc`) e as dependências de runtime estão em `requirements.txt` (não há `pyproject.toml` com `[project]`/`requires-python`). Ver `proposal.md` - Why para a motivação.

## Goals / Non-Goals

**Goals:**
- Rodar testes e lint/format automaticamente em todo PR contra `main`.
- Mesclar o PR automaticamente assim que essas validações passarem, sem exigir clique manual.

**Non-Goals:**
- Deploy (não há infraestrutura de deploy no repositório).
- Configurar exigência de revisão humana antes do merge (é uma decisão de política do repositório, não deste change).
- Cobrir outras branches além de `main` como alvo de merge automático.

## Decisions

- **Plataforma de CI: GitHub Actions.** O repositório já está no GitHub; usar Actions evita introduzir um serviço externo (CircleCI, Travis, etc.) só para isso.

- **Ferramenta de lint/format: `ruff`.** Cobre lint e format-check (`ruff check` + `ruff format --check`) em uma única ferramenta rápida, evitando combinar `flake8` + `black` + `isort` separadamente. Alternativa considerada: `flake8`/`black` — rejeitada por exigir mais configuração e mais um binário no pipeline sem ganho adicional para um projeto deste tamanho.

- **Gerenciamento da nova dependência: `requirements-dev.txt`.** Novo arquivo com `-r requirements.txt` mais `ruff`, mantendo `requirements.txt` (runtime/produção) livre de ferramentas de desenvolvimento. Alternativa considerada: adicionar `ruff` direto em `requirements.txt` — rejeitada por misturar dependência de dev com dependência de runtime.

- **Versão do Python no workflow: 3.13**, para espelhar o ambiente local (`venv` atual). Sem matriz de versões, já que o projeto não declara versões suportadas em `pyproject.toml`.

- **Mecanismo de merge automático: recurso nativo de auto-merge do GitHub** (`gh pr merge --auto --squash`, ou equivalente via API, disparado pelo workflow após os checks passarem), em vez de a Action fazer o merge diretamente. O auto-merge nativo só efetiva o merge quando **todos** os checks obrigatórios da branch protection passam — não só o desta Action — o que evita mesclar um PR que esteja passando neste workflow mas falhando em outro check obrigatório já existente ou futuro.

- **Trigger do workflow: evento `pull_request`** (não `pull_request_target`) tendo `main` como `base`. Mantém o comportamento padrão e mais seguro do GitHub Actions para PRs (token com permissões restritas em PRs de forks) — ver Risks abaixo para a limitação que isso impõe a PRs de forks.

- **Escopo do `ruff`: apenas `app/` e `tests/`**, tanto localmente quanto no workflow (`ruff check app tests` / `ruff format --check app tests`), em vez do repositório inteiro. Descoberto durante a implementação: rodar `ruff format --check .` sem escopo aponta 8 arquivos Markdown de referência de skills do Claude Code (`.agents/skills/`, `.claude/skills/`, `.codex/skills/`) como "não formatados" — esses arquivos não são código deste projeto e não devem ser reformatados por este change. Alternativa considerada: excluir esses diretórios via `extend-exclude` em um `ruff.toml`/`pyproject.toml` — rejeitada por ser mais um arquivo de configuração para o mesmo resultado que passar os paths explicitamente nos comandos.

## Risks / Trade-offs

- [Risk] PRs de repositórios forkados rodam com um `GITHUB_TOKEN` somente-leitura sob o evento `pull_request`, então o passo de auto-merge não terá permissão de habilitar o merge nesses PRs → Mitigation: documentar a limitação; PRs de forks continuam sendo validados (testes/lint rodam normalmente), mas o merge automático só funciona de forma confiável para PRs de branches dentro do próprio repositório. Habilitar auto-merge para forks é um passo manual fora de escopo.

- [Risk] Introduzir `ruff` pode apontar violações em código já existente, quebrando o primeiro run da CI por motivos não relacionados ao PR que a disparou → Mitigation: `tasks.md` inclui rodar `ruff check`/`ruff format --check` localmente e corrigir eventuais violações existentes antes de ativar o workflow como gate.

- [Risk] O auto-merge nativo do GitHub e a exigência deste check como obrigatório dependem de configurações do repositório (opção "Allow auto-merge" e branch protection rule em `main`) que não são versionadas em código → Mitigation: `tasks.md` lista esses passos como configuração manual explícita, com as instruções necessárias, em vez de assumir que já estão habilitados.

## Migration Plan

1. Adicionar `requirements-dev.txt` e o workflow `.github/workflows/ci.yml`.
2. Rodar `ruff` localmente e corrigir violações pré-existentes, se houver, para não quebrar o primeiro PR real após a ativação.
3. Abrir um PR de teste para validar que o workflow roda, reporta os checks corretamente e (com auto-merge habilitado no repositório) mescla sozinho quando tudo passa.
4. Habilitar manualmente, nas configurações do repositório: "Allow auto-merge" e uma branch protection rule em `main` exigindo o novo check antes do merge.
5. Rollback, se necessário: desabilitar "Allow auto-merge" e/ou remover o check da branch protection rule; o workflow pode continuar rodando apenas como validação (sem merge automático) ou ser removido.
