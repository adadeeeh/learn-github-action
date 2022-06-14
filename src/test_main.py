from urllib import response
from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200

def test_read_hello():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}