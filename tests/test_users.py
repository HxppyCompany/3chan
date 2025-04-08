import pytest
from fastapi import status
from fastapi.testclient import TestClient

from tests.client import api_client  # noqa: F401


@pytest.mark.parametrize(
    ["name", "password"],
    [
        ("user", "password"),
        ("user1", "qwerty12"),
        ("Вася", "12345678"),
        ("Петя", "2efrfergrtg"),
        ("wefegerg", "wdgrthrt"),
        ("1", "q13weferfewrf"),
        ("a", "dwert345y5y"),
    ],
)
def test_user_creation_valid(name: str, password: str, api_client: TestClient):
    user_schema = {
        "name": name,
        "password": password,
    }
    response = api_client.post("/users", json=user_schema)

    assert response.status_code == status.HTTP_200_OK

    data = response.json()
    assert "name" in data and data["name"] == name
    assert "password" not in data
    assert "id" in data and isinstance(data["id"], int)


@pytest.mark.parametrize(
    "password", ["qwerty12", "12345678", "qefewrgtertg", "qwewdefaf"]
)
def test_user_creation_invalid_name(password: str, api_client: TestClient):
    user_schema = {
        "name": "",
        "password": password,
    }
    response = api_client.post("/users", json=user_schema)

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


@pytest.mark.parametrize(
    ["name", "password"],
    [
        ("user", ""),
        ("user", "1"),
        ("user", "12345"),
        ("", ""),
        ("", "qwerty"),
    ],
)
def test_user_creation_invalid_password(
    name: str, password: str, api_client: TestClient
):
    user_schema = {
        "name": name,
        "password": password,
    }
    response = api_client.post("/users", json=user_schema)

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


@pytest.mark.parametrize(
    ["name", "password"],
    [
        ("user123123", "qwerty12"),
        ("123423f2f", "awdwdqf12"),
        ("1231eqwdw", "wedfwefwef"),
    ],
)
def test_user_creation_existing(name: str, password: str, api_client: TestClient):
    user_schema = {
        "name": name,
        "password": password,
    }
    response = api_client.post("/users", json=user_schema)

    assert response.status_code == status.HTTP_200_OK

    user_schema = {
        "name": name,
        "password": password,
    }
    response = api_client.post("/users", json=user_schema)

    assert response.status_code == status.HTTP_409_CONFLICT


@pytest.mark.parametrize("id", [1000, 2000, 50, 40, 100])
def test_user_get_not_found(id: int, api_client: TestClient):
    response = api_client.get(f"/users/{id}")

    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.parametrize(
    ["name", "password"],
    [
        ("user5", "password"),
        ("john", "qwerty1234"),
        ("peter", "12345678"),
        ("user12", "qwerty456"),
    ],
)
def test_user_get_existing(name: str, password: str, api_client: TestClient):
    user_schema = {
        "name": name,
        "password": password,
    }
    response = api_client.post("/users", json=user_schema)

    assert response.status_code == status.HTTP_200_OK

    data_1 = response.json()

    response = api_client.get(f"/users/{data_1['id']}")

    assert response.status_code == status.HTTP_200_OK

    data_2 = response.json()
    assert data_1 == data_2
