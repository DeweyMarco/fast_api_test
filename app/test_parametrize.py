import pytest
from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

'''
This test suite focuses on verifying the functionality of the 
API related to multiple entries

This test suite makes use of pytest's parametrize plugin
'''

testdata = [
    (
        {"id": 1, "text": "Add an item", "completed": False},
        200,
        {"id": 1, "text": "Add an item", "completed": True},
    ),
    (
        {"id": 2, "text": "Second item", "completed": False},
        200,
        {"id": 2, "text": "Second item", "completed": True},
    ),
    (
        {"id": 3, "text": "Last item", "completed": False},
        200,
        {"id": 3, "text": "Last item", "completed": True},
    ),
]

# Test creating a new to-do item
@pytest.mark.parametrize("initial_state, status, final_state", testdata)
def test_create_todo(initial_state, status, final_state):
    response = client.post(
        "/todos/",
        headers = {"X-Token": "password"},
        json = initial_state,
    )
    assert response.status_code == status
    assert response.json() == initial_state
    
# Tests updating the completed field an existing to-do item
@pytest.mark.parametrize("initial_state, status, final_state", testdata)
def test_update_completed(initial_state, status, final_state):
    response = client.put(
        "/todos/" + str(initial_state["id"]),
        headers = {"X-Token": "password"},
        json = final_state,
    )
    assert response.status_code == status
    assert response.json() == final_state
    
# Tests deleting all items in to-do list
@pytest.mark.parametrize("initial_state, status, final_state", testdata)
def test_delete(initial_state, status, final_state):
    response = client.delete(
        "/todos/" + str(initial_state["id"]),
        headers={"X-Token": "password"},
    )
    assert response.status_code == status
    assert response.json() == {
        "message": "Item deleted"
    }