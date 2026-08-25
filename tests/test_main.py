from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_predict_sentiment():
    payload = {"text": "Continuous Integration is awesome"}
    response = client.post("/predict", json=payload)
    
    assert response.status_code == 200
    assert response.json()["char_count"] == 33
    assert response.json()["processed"] is True
