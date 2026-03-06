from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

# Patron AAA
def test_create_user():

    payload = {
        "name": "Juan",
        "age": 30
    }

    response = client.post("/users/", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Juan"
    assert data["age"] == 30