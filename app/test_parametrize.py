import pytest
from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

'''
This test suite focuses on verifying the functionality of the 
API related to multiple entries

This test suite makes use of pytest's parametrize plugin. 

Run with 
$ pytest app/test_parametrize.py --cov=app.main


Database (testdata)

password - json

initial_state - json

status - integer

final_state - json

error_message -json

'''

testdata = [
    (
        {"X-Token": "password"},
        {"id": 1, "text": "Add an item", "completed": False},
        200,
        {"id": 4, "text": "Change item", "completed": True},
        {},
    ),
    (
        {"X-Token": "password"},
        {"id": 2, "text": "Second item", "completed": False},
        200,
        {"id": 5, "text": "Change second item", "completed": True},
        {},
    ),
    (
        {"X-Token": "password"},
        {"id": 3, "text": "Last item", "completed": False},
        200,
        {"id": 6, "text": "Change last item", "completed": True},
        {},
    ),
    (
        {"X-Token": "password"},
        {"id": 1, "text": "Bad item", "completed": False},
        401,
        {},
        {"detail": "Item ID already in use"},
    ),
    (
        {"X-Token": "12345678"},
        {"id": 1, "text": "Bad password", "completed": False},
        400,
        {},
        {"detail": "Invalid X-Token header"},
    ),
    (
        {"X-Token": "password"},
        {"id": 9, "text": "Not in list", "completed": False},
        404,
        {},
        {"detail": "Item not found"},
    ),
]

# Test creating a new to-do item (post)
@pytest.mark.parametrize("password, initial_state, status, final_state, error_message", testdata)
def test_create_todo(password, initial_state, status, final_state, error_message):
    if status == 200:
        response = client.post(
            "/todos/",
            headers = password,
            json = initial_state,
        )
        assert response.status_code == status
        assert response.json() == initial_state
    elif status == 401:
        response = client.post(
            "/todos/",
            headers = password,
            json = initial_state,
        )
        assert response.status_code == status
        assert response.json() == error_message
    elif status == 400:
        response = client.post(
            "/todos/",
            headers = password,
            json = initial_state,
        )
        assert response.status_code == status
        assert response.json() == error_message
    elif status == 404:
        pass
    else:
        pass
        
# Test retrieving a to-do item (get)
@pytest.mark.parametrize("password, initial_state, status, final_state, error_message", testdata)
def test_get_todo(password, initial_state, status, final_state, error_message):
    if status == 200:
        response = client.get(
            "/todos/" + str(initial_state["id"]),
            headers = password,
        )
        assert response.status_code == status
        assert response.json() == initial_state
    elif status == 401:
        pass
    elif status == 400 or status == 404:
        response = client.get(
            "/todos/" + str(initial_state["id"]),
            headers = password,
        )
        assert response.status_code == status
        assert response.json() == error_message
    else:
        pass
    
# Test retrieving a to-do item (get all)
@pytest.mark.parametrize("password, initial_state, status, final_state, error_message", testdata)
def test_get_all_todo(password, initial_state, status, final_state, error_message):
    if status == 200:
        response = client.get(
            "/todos/",
            headers = password,
        )
        assert response.status_code == status
        assert response.json()[(initial_state["id"]) - 1] == initial_state
    elif status == 401 or status == 404:
        pass
    elif status == 400:
        response = client.get(
            "/todos/",
            headers = password,
        )
        assert response.status_code == status
        assert response.json() == error_message
    else:
        pass
    
# Test changing a to-do item (put)
@pytest.mark.parametrize("password, initial_state, status, final_state, error_message", testdata)
def test_update_completed(password, initial_state, status, final_state, error_message):
    if status == 200:
        response = client.put(
            "/todos/" + str(initial_state["id"]),
            headers = password,
            json = final_state,
        )
        assert response.status_code == status
        assert response.json() == final_state
    elif status == 401:
        pass
    elif status == 400 or status == 404:
        response = client.put(
            "/todos/" + str(initial_state["id"]),
            headers = password,
            json = initial_state,
        )
        assert response.status_code == status
        assert response.json() == error_message
    else:
        pass
    
# Tests deleting a to-do item (delete)
@pytest.mark.parametrize("password, initial_state, status, final_state, error_message", testdata)
def test_delete(password, initial_state, status, final_state, error_message):
    if status == 200:
        response = client.delete(
            "/todos/" + str(initial_state["id"]),
            headers = password,
        )
        assert response.status_code == status
        assert response.json() == {
            "message": "Item deleted"
        }
    elif status == 401:
        pass
    elif status == 400 or status == 404:
        response = client.delete(
            "/todos/" + str(initial_state["id"]),
            headers = password,
        )
        assert response.status_code == status
        assert response.json() == error_message
    else:
        pass