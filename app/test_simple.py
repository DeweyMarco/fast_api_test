import pytest
from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

'''
This test suite focuses on verifying the functionality of the 
API related to a single to-do list item

Steps
1. Create an item in the to-do list (post)
2. Verify that the item is in the to-do list (get all)
3. Get the item in the to-do list (get)
4. Edit the item in the to-do list (put)
    a. completed field
    b. text field
    c. id field
5. Verify that there is still one item in the to-do list (get all)
6. Get the edited item in the to-do list (get)
7. Delete the edited item in the to-do list (delete)
8. Verify that there are no items in the to-do list (get all)
'''

# Test creating a new to-do item
def test_create_todo():
    response = client.post(
        "/todos/",
        headers={"X-Token": "password"},
        json={"id": 1, "text": "Add an item", "completed": False},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "text": "Add an item",
        "completed": False,
    }
    
# Test if there is one item in the to-do list
def test_one_item():
    response = client.get(
        "/todos/",
        headers={"X-Token": "password"},
    )
    assert response.status_code == 200
    assert len(response.json()) == 1
    
# Test getting the item from the to-do list
def test_get_item():
    response = client.get(
        "/todos/1",
        headers={"X-Token": "password"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "text": "Add an item",
        "completed": False,
    }
    
# Tests updating the completed field an existing to-do item
def test_update_completed():
    response = client.put(
        "/todos/1",
        headers={"X-Token": "password"},
        json={"id": 1, "text": "Add an item", "completed": True},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "text": "Add an item",
        "completed": True,
    }
    
# Tests updating the text field an existing to-do item
def test_update_text():
    response = client.put(
        "/todos/1",
        headers={"X-Token": "password"},
        json={"id": 1, "text": "Edit the text", "completed": True},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "text": "Edit the text",
        "completed": True,
    }
    
# Tests updating the id field an existing to-do item
def test_update_id():
    response = client.put(
        "/todos/1",
        headers={"X-Token": "password"},
        json={"id": 2, "text": "Edit the text", "completed": True},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 2,
        "text": "Edit the text",
        "completed": True,
    }
    
# Test if there is one item in the to-do list
def test_verify_one_item():
    response = client.get(
        "/todos/",
        headers={"X-Token": "password"},
    )
    assert response.status_code == 200
    assert len(response.json()) == 1
    
# Test getting the item from the to-do list
def test_verify_get_item():
    response = client.get(
        "/todos/1",
        headers={"X-Token": "password"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 2,
        "text": "Edit the text",
        "completed": True,
    }
    
# Test deleting if the to-do list is not empty
def test_delete():
    response = client.delete(
        "/todos/1",
        headers={"X-Token": "password"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "message": "Item deleted"
    }
    
# Test if there is one item in the to-do list
def test_verify_zero_item():
    response = client.get(
        "/todos/",
        headers={"X-Token": "password"},
    )
    assert response.status_code == 200
    assert len(response.json()) == 0