from flask import Blueprint, g, jsonify, request
from marshmallow import ValidationError

from database.crud import orm_update_task
from database.engine import SessionLocal
from schemas import TaskSchema_update

bp = Blueprint("update_task", __name__)
task_schema = TaskSchema_update()


@bp.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    if not request.is_json:
        return jsonify({"error": "Unsupported Media Type"}), 415

    data = request.get_json()
    try:
        validated_data = task_schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    title = validated_data.get("title", None)
    description = validated_data.get("description", None)
    task = orm_update_task(g.db_session, task_id, title, description)

    if task is None:
        return jsonify({"error": "Task not found"}), 404

    response_data = task_schema.dump(task)
    return jsonify(response_data), 200
