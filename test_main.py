from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_division():
    response = client.post(
        "/divide",
        json={"num1": 20, "num2": 5}
    )

    assert response.status_code == 200
    assert response.json()["result"] == 4.0


def test_decimal_division():
    response = client.post(
        "/divide",
        json={"num1": 10, "num2": 4}
    )

    assert response.status_code == 200
    assert response.json()["result"] == 2.5


def test_division_by_zero():
    response = client.post(
        "/divide",
        json={"num1": 10, "num2": 0}
    )

    assert response.status_code == 400


def test_negative_numbers():
    response = client.post(
        "/divide",
        json={"num1": -20, "num2": 5}
    )

    assert response.status_code == 200
    assert response.json()["result"] == -4.0