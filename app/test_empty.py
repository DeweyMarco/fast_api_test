import pytest
from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

'''
This test suite focuses on verifying the functionality of the 
API related to an empty to-do list
'''

# Test if the to-do list is empty at initiation
def test_empty():
    response = client.get(
        "/todos/",
        headers={"X-Token": "password"},
    )
    assert response.status_code == 200
    assert len(response.json()) == 0
    
# Test deleting if the to-do list is empty
def test_empty_delete():
    response = client.delete(
        "/todos/1",
        headers={"X-Token": "password"},
    )
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Item not found"
    }
    
# Test updating an item that does not exist
def test_update_no_item():
    response = client.put(
        "/todos/1",
        headers={"X-Token": "password"},
        json={"id": 1, "text": "Buy groceries", "completed": True},
    )
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Item not found"
    }
    
# Test getting an item that does not exist
def test_get_todo():
    response = client.get(
        "/todos/1", 
        headers={"X-Token": "password"},
    )
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Item not found"
    }
    