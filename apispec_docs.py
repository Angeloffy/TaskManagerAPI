from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin

from schemas import TaskSchema, TaskSchema_update


def get_apispec(app):
    spec = APISpec(
        title="Task API",
        version="1.0.0",
        openapi_version="3.0.3",
        plugins=[MarshmallowPlugin()],
    )
    with app.test_request_context():
        spec.components.schema("Task", schema=TaskSchema)
        spec.components.schema("TaskSchema_update", schema=TaskSchema_update)

    spec.path(
        path="/tasks",
        operations={
            "post": {
                "responses": {
                    "201": {
                        "description": "Created",
                        "schema": {"$ref": "#/components/schemas/Task"},
                    }
                },
                "summary": "Create a new task",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/Task"}
                        }
                    }
                },
            }
        },
    )

    spec.path(
        path="/tasks/{task_id}",
        parameters=[
            {
                "name": "task_id",
                "in": "path",
                "required": True,
                "schema": {"type": "integer"},
                "description": "ID of the task",
            }
        ],
        operations={
            "get": {
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {"$ref": "#/components/schemas/Task"},
                    },
                    "404": {"description": "Task not found"},
                },
                "summary": "Get a task by ID",
            }
        },
    )

    spec.path(
        path="/tasks",
        operations={
            "get": {
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "type": "array",
                            "items": {"$ref": "#/components/schemas/Task"},
                        },
                    }
                },
                "summary": "Get all tasks",
            }
        },
    )

    spec.path(
        path="/tasks/{task_id}",
        parameters=[
            {
                "name": "task_id",
                "in": "path",
                "required": True,
                "schema": {"type": "integer"},
                "description": "ID of the task to delete",
            }
        ],
        operations={
            "delete": {
                "responses": {
                    "200": {"description": "OK"},
                    "404": {"description": "Task not found"},
                },
                "summary": "Delete a task by ID",
            }
        },
    )

    spec.path(
        path="/tasks/{task_id}",
        parameters=[
            {
                "name": "task_id",
                "in": "path",
                "required": True,
                "schema": {"type": "integer"},
                "description": "ID of the task",
            }
        ],
        operations={
            "put": {
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {"$ref": "#/components/schemas/Task"},
                    },
                    "400": {"description": "Bad Request"},
                    "404": {"description": "Task not found"},
                },
                "summary": "Update a task by ID",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/TaskSchema_update"}
                        }
                    }
                },
            }
        },
    )

    return spec
