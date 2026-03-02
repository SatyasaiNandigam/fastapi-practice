from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_home():
    response = client.get("/")
    assert response.status_code == 200
    # Add an assertion for whatever your home page returns
    assert response == "My home"
    
def test_read_cart():
    response = client.get("/cart")
    assert response.status_code == 200
    assert response.json() == {"response": "carts here"}