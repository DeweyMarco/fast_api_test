# fast_api_test

This project is a simple REST API for managing to-do items built with FastAPI

### Features

    Create new to-do items
    Get a list of all to-do items
    Get a specific to-do item by ID
    Update a to-do item
    Delete a to-do item

### API Endpoints

    GET /todos/: Retrieve a list of all to-do items.
    POST /todos/: Create a new to-do item. The request body should be a 
    GET /todos/{todo_id}: Get a specific to-do item by its ID.
    PUT /todos/{todo_id}: Update a to-do item with the provided data in the request body.
    DELETE /todos/{todo_id}: Delete a to-do item by its ID.

### Testing
```
pytest
```