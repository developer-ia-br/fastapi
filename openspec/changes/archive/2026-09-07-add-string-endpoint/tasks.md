## 1. Schema e Router

- [x] 1.1 Criar `app/schemas/strings.py` com o modelo de resposta (`result: str`) e verificar que o import funciona sem erros
- [x] 1.2 Criar `app/api/strings.py` com um `APIRouter` (`prefix="/str"`, `tags=["strings"]`) e o endpoint `GET /{value}`, que recebe `value: str` via `Annotated[str, Path(...)]` e retorna `value + "X"` no schema de resposta
- [x] 1.3 Registrar o novo router em `app/main.py` (`app.include_router(strings_router)`) e verificar que a aplicação sobe sem erros (`fastapi dev` ou `TestClient(app)`)

## 2. Testes

- [x] 2.1 Adicionar teste cobrindo `GET /str/{value}` com um valor não vazio e verificar `200 OK` com `{"result": value + "X"}`
- [x] 2.2 Rodar a suíte completa (`python -m pytest -q`) e verificar que todos os testes passam
