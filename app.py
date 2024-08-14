from fastapi import FastAPI, Body, HTTPException, status
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Define a Pydantic model for the to-do item data
class Todo(BaseModel):
    text: str
    completed: bool = False

# In-memory list of to-do items (replace with a database for production)
todos: list[Todo] = [
    Todo(text="Buy groceries", completed=False),
    Todo(text="Learn Python", completed=False),
    Todo(text="Build a REST API", completed=False),
]


# Get all to-do items
@app.get("/todos", response_model=list[Todo])
def get_todos():
    return todos


# Create a new to-do item
@app.post("/todos", response_model=Todo, status_code=status.HTTP_201_CREATED)
def create_todo(todo: Todo = Body(...)):
    todo.id = len(todos) + 1
    todos.append(todo)
    return todo


# Get a specific to-do item
@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    todo = find_todo(todo_id)
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return todo


# Update a specific to-do item
@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: Todo = Body(...)):
    todo = find_todo(todo_id)
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    todo.update(updated_todo)
    return todo


# Delete a specific to-do item
@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int):
    todo = find_todo(todo_id)
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    todos.remove(todo)
    return None  # No content to return on successful deletion


# Helper function to find a to-do item by ID
def find_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return None

# Run the API server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)