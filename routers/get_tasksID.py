from flask import Blueprint, jsonify, g
from database.crud import orm_get_task_by_id
from database.engine import SessionLocal
from schemas import task_schema

bp = Blueprint('get_task', __name__)


@bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = SessionLocal()

    task = orm_get_task_by_id(db, task_id)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404

    response_data = task_schema.dump(task)
    return jsonify(response_data), 200
