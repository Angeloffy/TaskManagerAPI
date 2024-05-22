import pytest

from app import app as flask_app


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_create_task(client):
    # Проверка создания новой задачи
    task_data = {"title": "Test Task", "description": "This is a test task"}
    response = client.post("/tasks", json=task_data)
    # Проверка успешного создания задачи
    assert response.status_code == 201

    response_data = response.json
    # Проверка наличия полей в ответе
    assert "id" in response_data
    assert "created_at" in response_data
    assert "updated_at" in response_data
    assert "title" in response_data
    assert response_data["title"] == task_data["title"]
    assert "description" in response_data
    assert response_data["description"] == task_data["description"]


def test_get_task_by_id(client):
    # Проверка получения информации о задаче по идентификатору
    task_data = {"title": "Test Task", "description": "This is a test task"}
    response = client.post("/tasks", json=task_data)
    assert response.status_code == 201
    task_id = response.json["id"]

    response = client.get(f"/tasks/{task_id}")
    # Проверка успешного получения информации о задаче
    assert response.status_code == 200
    # Проверка наличия необходимых полей в ответе
    response_data = response.json
    assert "id" in response_data
    assert "created_at" in response_data
    assert "updated_at" in response_data
    assert "title" in response_data
    assert "description" in response_data


def test_update_task(client):
    # Проверка обновления задачи
    task_data = {"title": "Test Task", "description": "This is a test task"}
    response = client.post("/tasks", json=task_data)
    assert response.status_code == 201
    task_id = response.json["id"]

    updated_task_data = {
        "title": "Updated Test Task",
        "description": "This is an updated test task",
    }
    response = client.put(f"/tasks/{task_id}", json=updated_task_data)
    # Проверка успешного обновления задачи
    assert response.status_code == 200

    response_data = response.json
    # Проверка наличия необходимых полей в ответе
    assert "id" in response_data
    assert "created_at" in response_data
    assert "updated_at" in response_data
    assert "title" in response_data
    assert response_data["title"] == updated_task_data["title"]
    assert "description" in response_data
    assert response_data["description"] == updated_task_data["description"]


def test_delete_task(client):
    # Проверка удаления задачи
    task_data = {"title": "Test Task", "description": "This is a test task"}
    response = client.post("/tasks", json=task_data)
    assert response.status_code == 201
    task_id = response.json["id"]

    # Удаляем задачу
    response = client.delete(f"/tasks/{task_id}")
    # Проверка успешного удаления задачи
    assert response.status_code == 200

    response = client.get(f"/tasks/{task_id}")
    # Проверка, что задача больше не доступна
    assert response.status_code == 404


def test_get_all_tasks(client):
    # Проверка получения списка всех задач
    response = client.get("/tasks")
    assert response.status_code == 200
    response_data = response.json
    # Проверка формата и содержания списка задач
    assert isinstance(response_data, list)
    assert len(response_data) >= 1
    for task in response_data:
        assert "id" in task
        assert "created_at" in task
        assert "updated_at" in task
        assert "title" in task
        assert "description" in task
