import pytest
# from allure_pytest import allure_step, attach
from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_get_todos():
    response = client.get("/todos")
    assert response.status_code == 200
    assert len(response.json()) == 3

# def test_create_todo():
#     new_todo = {"text": "New Todo", "completed": False}
#     response = client.post("/todos", json=new_todo)
#     assert response.status_code == 201
#     assert response.json()["text"] == "New Todo"
#     assert response.json()["completed"] is False

# def test_get_todo():
#     response = client.get("/todos/1")
#     assert response.status_code == 200
#     assert response.json()["id"] == 1
#     assert response.json()["text"] == "Buy groceries"

# def test_update_todo():
#     updated_todo = {"text": "Updated Todo", "completed": True}
#     response = client.put("/todos/1", json=updated_todo)
#     assert response.status_code == 200
#     assert response.json()["text"] == "Updated Todo"
#     assert response.json()["completed"] is True

# def test_delete_todo():
#     response = client.delete("/todos/1")
#     assert response.status_code == 204
#     response = client.get("/todos/1")
#     assert response.status_code == 404  