from fastapi.testclient import TestClient


def test_health(client: TestClient) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_get_item_found(client: TestClient) -> None:
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Widget"


def test_get_item_not_found(client: TestClient) -> None:
    response = client.get("/items/999")
    assert response.status_code == 404


def test_get_item_below_minimum_id(client: TestClient) -> None:
    response = client.get("/items/0")
    assert response.status_code == 422


def test_get_item_invalid_id_type(client: TestClient) -> None:
    response = client.get("/items/abc")
    assert response.status_code == 422


def test_double_valid_integer(client: TestClient) -> None:
    response = client.get("/math/double/5")
    assert response.status_code == 200
    assert response.json() == {"result": 10}


def test_double_invalid_value_type(client: TestClient) -> None:
    response = client.get("/math/double/abc")
    assert response.status_code == 422


def test_ci_gate_intentionally_fails(client: TestClient) -> None:
    """Temporary: validates that CI blocks merge on a failing test (task 4.3)."""
    assert False
