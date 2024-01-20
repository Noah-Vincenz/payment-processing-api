import pytest

from fastapi.testclient import TestClient
from src.app import app


@pytest.fixture
def api_client() -> TestClient:
    return TestClient(app)


@pytest.fixture
def token(api_client: TestClient) -> str:
    response = api_client.post(
        "/tokens",
        json={
            "cardholder_name": "Joe Bloggs",
            "card_number": "4111111111111111",
            "cvv": "123",
            "expiry_year": "2023",
            "expiry_month": "1",
        },
    )
    data = response.json()
    return data["token"]


def test_payment_authorization_succeeds_against_midas(
    api_client: TestClient, token: str
):
    response = api_client.post(
        "/payments",
        json={
            "token": token,
            "processor_id": "MIDAS",
            "amount": 1.23,
            "currency_code": "EUR",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "AUTHORIZED"
    assert isinstance(data["processor_transaction_id"], str)


def test_payment_authorization_is_declined_against_achilles(
    api_client: TestClient, token: str
):
    response = api_client.post(
        "/payments",
        json={
            "token": token,
            "processor_id": "ACHILLES",
            "amount": 1.23,
            "currency_code": "EUR",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "DECLINED"
    assert isinstance(data["processor_transaction_id"], str)
