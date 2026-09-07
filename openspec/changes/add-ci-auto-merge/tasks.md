## 1. Dependências de desenvolvimento

- [x] 1.1 Criar `requirements-dev.txt` com `-r requirements.txt` mais `ruff`, e verificar que `pip install -r requirements-dev.txt` conclui sem erro
- [x] 1.2 Rodar `ruff check app tests` e `ruff format --check app tests` localmente (escopo restrito a `app/` e `tests/` — ver `design.md` Decisions) e corrigir quaisquer violações encontradas, verificando que ambos os comandos retornam sem erro após as correções

## 2. Workflow de CI

- [x] 2.1 Criar `.github/workflows/ci.yml` com um job que instala as dependências de `requirements-dev.txt` e roda `pytest -q`, disparado no evento `pull_request` com `main` como branch alvo; verificar que o arquivo é YAML válido
- [x] 2.2 Adicionar ao mesmo job (ou a um job irmão) os passos `ruff check app tests` e `ruff format --check app tests`; verificar que o workflow reporta teste e lint como checks separados (ou etapas visíveis) no PR de teste da seção 4
- [x] 2.3 Adicionar um job/step de auto-merge que roda apenas após teste e lint terem sucesso (`needs:`/`if: success()`), chamando o auto-merge nativo do GitHub (`gh pr merge --auto --squash`) com as permissões `pull-requests: write` e `contents: write` declaradas no workflow; verificar que o passo é pulado quando teste ou lint falham

## 3. Configuração manual do repositório (fora do código versionado)

- [x] 3.1 Habilitar a opção "Allow auto-merge" nas configurações do repositório no GitHub e verificar que ela aparece marcada em Settings > General
- [x] 3.2 Criar uma branch protection rule para `main` exigindo o check de CI deste workflow antes do merge, e verificar que um PR de teste mostra esse check como obrigatório

## 4. Validação end-to-end

- [ ] 4.1 Abrir um pull request de teste contra `main` e verificar que os checks de teste e lint aparecem e passam
- [ ] 4.2 Confirmar que o PR de teste é mesclado automaticamente assim que os checks passam, verificando pelo histórico do PR que o merge foi feito pela Action, não manualmente
- [ ] 4.3 Abrir um segundo PR de teste que falhe propositalmente (teste ou lint quebrado) e verificar que ele permanece sem merge com o check reportando falha
