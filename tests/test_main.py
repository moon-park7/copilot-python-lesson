from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_generate():
    response = client.post("/generate", json={"length": 10})
    assert response.status_code == 200
    assert "token" in response.json()
    assert len(response.json()["token"]) == 10
