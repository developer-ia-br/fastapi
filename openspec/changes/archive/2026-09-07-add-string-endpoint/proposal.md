## Why

A API atualmente expõe apenas os recursos `health`, `items` e `math`. Não existe nenhum endpoint para operações simples sobre strings, e um cliente precisa de uma forma de concatenar um sufixo fixo a um valor de texto via API (rascunho registrado em `docs/endpointString.md`).

## What Changes

- Adicionar um novo router `strings` (`app/api/strings.py`) com o endpoint `GET /str/{value}`.
- O endpoint aceita um parâmetro de path `value` do tipo string e retorna `value` concatenado com o sufixo `"X"` como JSON (`{"result": value + "X"}`).
- Registrar o novo router em `app/main.py`.

## Capabilities

### New Capabilities
- `strings`: operações utilitárias sobre strings expostas via API, começando pela concatenação de um sufixo fixo a um valor recebido.

### Modified Capabilities
(nenhuma)

## Impact

- Novo arquivo: `app/api/strings.py` (router) e seu schema de resposta em `app/schemas/strings.py`.
- Modificado: `app/main.py` (inclusão do novo router).
- Novos testes cobrindo o endpoint em `tests/`.
- Sem alterações no comportamento existente de `items`, `health` ou `math`.
- Assunção: como `value` é tipado como `str`, qualquer valor de path é aceito — não existe um caso de rejeição por "valor inválido" equivalente ao `422` do endpoint `math.double` (que só ocorre para tipos não-string, como `int`). O rascunho em `docs/endpointString.md` continha esse cenário por analogia ao endpoint `math`, mas ele não se aplica a um parâmetro string.
- Fora de escopo deste change: a criação de um PR draft no GitHub (mencionada no rascunho) é uma ação de implementação/entrega, não parte do planejamento OpenSpec — deverá ser tratada durante ou após a fase de apply.
