# TaskManagerAPI

## Installation
To install the dependencies for TaskManagerAPI, navigate to the project directory and run the following command:
```bash
poetry install
```

## Setting up Environment Variables in .env File
*Path: config/.env*

To configure the necessary environment variables for the MySQL database in the .env file, you should specify the following information:
````
MYSQL_HOST=
MYSQL_PORT=
MYSQL_DB=
MYSQL_USER=
MYSQL_PASSWORD=
`````

## Usage
Once the dependencies are installed, you can start the TaskManagerAPI by running the following command:
```bash
poetry run python app.py
```

This will start the API server, and it will be accessible at http://localhost:5000.

## Endpoints

### Create a Task
- URL: /tasks
- Method: POST
- Description: Creates a new task.
- Request Body: JSON data representing the task to be created.
- Response: Returns the created task data if successful, along with a status code of 201.
- Example:
```json
{
  "title": "Task Title",
  "description": "Task Description"
}
````

### Delete a Task
- URL: /tasks/<task_id>
- Method: DELETE
- Description: Deletes the task with the specified ID.
- Response: Returns a success message if the task is successfully deleted, along with a status code of 200.

### Get All Tasks
- URL: /tasks
- Method: GET
- Description: Retrieves all tasks.
- Response: Returns a list of all tasks along with a status code of 200.

### Get a Task
- URL: /tasks/<task_id>
- Method: GET
- Description: Retrieves a specific task by its ID.
- Response: Returns the task data if found, along with a status code of 200.

### Update a Task
- URL: /tasks/<task_id>
- Method: PUT
- Description: Updates the task with the specified ID.
- Request Body: JSON data representing the updated task information.
- Response: Returns the updated task data if successful, along with a status code of 200.
- Example:
```json
{
  "title": "Updated Task Title",
  "description": "Updated Task Description"
}
```

For more detailed documentation on the API endpoints, please refer to the `/docs` route.
