import pytest
from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

'''
This test suite focuses on verifying the functionality of the 
API related to authentication using the X-Token header

The correct X-Token is "password"
'''

# Test if an invalid token returns a 400 Bad Request response (get all)
def test_bad_token_get_all():
    response = client.get(
        "/todos/",
        headers={"X-Token": "12345678"},
    )
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Invalid X-Token header"
    }
    
# Test if an invalid token returns a 400 Bad Request response (get)
def test_bad_token_get():
    response = client.get(
        "/todos/1", 
        headers={"X-Token": "PASSWORD"},
    )
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Invalid X-Token header"
    }
    
# Test if an invalid token returns a 400 Bad Request response (post)
def test_bad_token_post():
    response = client.post(
        "/todos/",
        headers={"X-Token": "!@#$%^&*"},
        json={"id": 1, "text": "Add an item", "completed": False},
    )
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Invalid X-Token header"
    }
    
# Test if an invalid token returns a 400 Bad Request response (delete)
def test_bad_token_delete():
    response = client.delete(
        "/todos/1",
        headers={"X-Token": "\n\t\'\'\"\b\f"},
    )
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Invalid X-Token header"
    }
    
# Test if an invalid token returns a 400 Bad Request response (put)
def test_bad_token_put():
    response = client.put(
        "/todos/1",
        headers={"X-Token": ""},
        json={"id": 1, "text": "Buy groceries", "completed": True},
    )
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Invalid X-Token header"
    }
    