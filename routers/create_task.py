from flask import Blueprint, g, jsonify, request
from marshmallow import ValidationError

from database.crud import orm_create_task
from schemas import task_schema

bp = Blueprint("add_task", __name__)


@bp.route("/tasks", methods=["POST"])
def create_task():
    if not request.is_json:
        return jsonify({"error": "Unsupported Media Type"}), 415

    data = request.get_json()
    try:
        validated_data = task_schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_task = orm_create_task(g.db_session, **validated_data)

    response_data = task_schema.dump(new_task)
    return jsonify(response_data), 201
