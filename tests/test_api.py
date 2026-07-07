from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "hello world i am changing the home message from feature branch"

def test_health():
    response = client.get("/health")
    assert response.status_code == 200