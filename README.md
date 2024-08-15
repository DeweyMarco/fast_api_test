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

## Testing

### Notes
When writing test cases with pytest for an API one should note that the API is only instated once so if your individual test file must assume that there is nothing in the to-do list and it must finish testing with nothing in the to-do list. 

Otherwise unintended errors may trigger in other test files.

Further test files should be checked to verify that function names are not duplicated.

### Running Tests
Run all tests
```
$ pytest
```

Run a spesific test file
```
$ pytest [path to file]
```

For example
```
$ pytest app/test_bad_token.py
```