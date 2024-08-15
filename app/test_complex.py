import pytest
from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

'''
This test suite focuses on verifying the functionality of the 
API related to multiple to-do list items

Steps
1.  Create 3 items in the to-do list (post X3)
2.  Verify that 3 items are in the to-do list (get all)
3.  Get the 3 items in the to-do list (get X3)
4.  Attempt to change one items id to another (put)
        This should not be possible
5.  Attempt to add an item to the to-do list with an id already in the list (put)   
        This should not be possible
6.  Delete the third item in the to-do list (delete)
7.  Create a new item in the to-do list with id #4 (post)
8.  Verify that 3 items are in the to-do list (get all)
9.  Create a new item in the to-do list with id #3 (post)
10. Verify that 4 items are in the to-do list (get all)
11. Delete all items in to-do list (delete X4)
12. Verify that there are no items in the to-do list (get all)
'''

# Test creating a new to-do item
def test_create_todo_1():
    response = client.post(
        "/todos/",
        headers={"X-Token": "password"},
        json={"id": 1, "text": "Buy groceries", "completed": False},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "text": "Buy groceries",
        "completed": False,
    }
    
# Test creating a new to-do item
def test_create_todo_2():
    response = client.post(
        "/todos/",
        headers={"X-Token": "password"},
        json={"id": 2, "text": "Learn Python", "completed": False},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 2,
        "text": "Learn Python",
        "completed": False,
    }
    
# Test creating a new to-do item
def test_create_todo_3():
    response = client.post(
        "/todos/",
        headers={"X-Token": "password"},
        json={"id": 3, "text": "Build a REST API", "completed": False},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 3,
        "text": "Build a REST API",
        "completed": False,
    }
    
# Test if there are 3 items in the to-do list
def test_one_item():
    response = client.get(
        "/todos/",
        headers={"X-Token": "password"},
    )
    assert response.status_code == 200
    assert len(response.json()) == 3
    
# Test getting the item from the to-do list
def test_get_item_1():
    response = client.get(
        "/todos/1",
        headers={"X-Token": "password"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "text": "Buy groceries",
        "completed": False,
    }
    
# Test getting the item from the to-do list
def test_get_item_2():
    response = client.get(
        "/todos/2",
        headers={"X-Token": "password"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 2,
        "text": "Learn Python",
        "completed": False,
    }
    
# Test getting the item from the to-do list
def test_get_item_3():
    response = client.get(
        "/todos/3",
        headers={"X-Token": "password"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 3,
        "text": "Build a REST API",
        "completed": False,
    }
    
# Tests updating the completed field an existing to-do item
def test_update_bad_id():
    response = client.put(
        "/todos/1",
        headers={"X-Token": "password"},
        json={"id": 2, "text": "Buy groceries", "completed": False},
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Item ID already in use"}
    
# Test posting with an id already in the to-do list
def test_create_bad_todo():
    response = client.post(
        "/todos/",
        headers={"X-Token": "password"},
        json={"id": 1, "text": "Add an second item", "completed": False},
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Item already exists"}
    
# Test delete the third item in the to-do list
def test_delete_3():
    response = client.delete(
        "/todos/3",
        headers={"X-Token": "password"},
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Item deleted"}

# Test add a item with id #4
def test_create_todo_4():
    response = client.post(
        "/todos/",
        headers={"X-Token": "password"},
        json={"id": 4, "text": "Skip and ID number", "completed": False},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 4,
        "text": "Skip and ID number",
        "completed": False,
    }
    
# Test if the to-do list is has three elements
def test_3_items():
    response = client.get(
        "/todos/",
        headers={"X-Token": "password"},
    )
    assert response.status_code == 200
    assert len(response.json()) == 3
    
# Test add a item with id #3
def test_create_todo_new_3():
    response = client.post(
        "/todos/",
        headers={"X-Token": "password"},
        json={"id": 3, "text": "New item #3", "completed": False},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 3,
        "text": "New item #3",
        "completed": False,
    }
    
# Test if the to-do list is has three elements
def test_4_items():
    response = client.get(
        "/todos/",
        headers={"X-Token": "password"},
    )
    assert response.status_code == 200
    assert len(response.json()) == 4
    
# Test deleting if the to-do list is not empty
def test_delete_1():
    response = client.delete(
        "/todos/1",
        headers={"X-Token": "password"},
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Item deleted"}
    
# Test deleting if the to-do list is not empty
def test_delete_2():
    response = client.delete(
        "/todos/2",
        headers={"X-Token": "password"},
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Item deleted"}
    
# Test deleting if the to-do list is not empty
def test_delete_new_3():
    response = client.delete(
        "/todos/3",
        headers={"X-Token": "password"},
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Item deleted"}
    
# Test deleting if the to-do list is not empty
def test_delete_4():
    response = client.delete(
        "/todos/4",
        headers={"X-Token": "password"},
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Item deleted"}
    
# Test if the to-do list is empty at initiation
def test_empty():
    response = client.get(
        "/todos/",
        headers={"X-Token": "password"},
    )
    assert response.status_code == 200
    assert len(response.json()) == 0