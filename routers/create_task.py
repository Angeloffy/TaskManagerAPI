from flask import Blueprint, request, jsonify, g

from database.crud import orm_create_task
from database.engine import SessionLocal
from schemas import task_schema
from marshmallow import ValidationError


bp = Blueprint('add_task', __name__)


@bp.route('/tasks', methods=['POST'])
def create_task():
    if not request.is_json:
        return jsonify({"error": "Unsupported Media Type"}), 415

    data = request.get_json()
    try:
        validated_data = task_schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = SessionLocal()
    new_task = orm_create_task(db, **validated_data)

    response_data = task_schema.dump(new_task)
    return jsonify(response_data), 201
