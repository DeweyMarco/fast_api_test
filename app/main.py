from fastapi import FastAPI, Body, HTTPException, status, Header
from pydantic import BaseModel
from typing import Annotated, List
import uvicorn

token = "password"

db = {}

app = FastAPI()

class Todo(BaseModel):
    id: int
    text: str
    completed: bool = False

# Get all to-do items  
@app.get("/todos/", response_model=List[Todo])
async def get_all_todos(x_token: Annotated[str, Header()]):
    if x_token != token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    return list(db.values())

# Get a specific to-do item
@app.get("/todos/{item_id}", response_model=Todo)
async def get_todo(item_id : int, x_token: Annotated[str, Header()]):
    if x_token != token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    return db[item_id]

# Create a new to-do item
@app.post("/todos/", response_model=Todo)
async def create_todo(item: Todo, x_token: Annotated[str, Header()]):
    if x_token != token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if item.id in db:
        raise HTTPException(status_code=401, detail="Item ID already in use")
    db[item.id] = item
    return item

# Delete a to-do item
@app.delete("/todos/{item_id}")
async def delete_todo(item_id: int, x_token: Annotated[str, Header()]):
    if x_token != token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    del db[item_id]
    return {"message": "Item deleted"}

# Update a to-do item
@app.put("/todos/{item_id}", response_model=Todo)
async def update_todo(item_id: int, updated_item: Todo, x_token: Annotated[str, Header()]):
    if x_token != token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    if updated_item.id != item_id and updated_item.id in db:
        raise HTTPException(status_code=401, detail="Item ID already in use")
    db[item_id] = updated_item
    return updated_item