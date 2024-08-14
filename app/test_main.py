import pytest
from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

# Tests if an invalid token returns a 400 Bad Request response
def test_bad_token():
    response = client.get("/todos/", headers={"X-Token": "12345678"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid X-Token header"}

# Tests retrieving all to-do items
def test_get_all_todos():
    response = client.get("/todos/", headers={"X-Token": "password"})
    assert response.status_code == 200
    assert len(response.json()) == 3

# Tests retrieving a specific to-do item
def test_get_todo():
    response = client.get("/todos/1", headers={"X-Token": "password"})
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "text": "Buy groceries",
        "completed": False,
    }

# Tests attempting to retrieve a non-existent to-do item. 
def test_get_bad_todo():
    response = client.get("/todos/0", headers={"X-Token": "password"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}
    
# Tests creating a new to-do item
def test_create_todo():
    response = client.post(
        "/todos/",
        headers={"X-Token": "password"},
        json={"id": 4, "text": "Add an item", "completed": False},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 4,
        "text": "Add an item",
        "completed": False,
    }

# Tests updating an existing to-do item
def test_update_todo():
    response = client.put(
        "/todos/1",
        headers={"X-Token": "password"},
        json={"id": 1, "text": "Buy groceries", "completed": True},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "text": "Buy groceries",
        "completed": True,
    }

# Test updating a non-existent to-do item
def test_bad_update_todo():
    response = client.put(
        "/todos/0",
        headers={"X-Token": "password"},
        json={"id": 0, "text": "Bad update", "completed": False},
    )
    assert response.status_code == 400