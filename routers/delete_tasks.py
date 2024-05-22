from flask import Blueprint, jsonify, g

from database.crud import orm_delete_task
from database.engine import SessionLocal

bp = Blueprint('delete_task', __name__)

@bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = SessionLocal()

    success = orm_delete_task(db, task_id)

    if not success:
        return jsonify({'error': 'Task not found'}), 404

    return jsonify({'message': 'Task successfully deleted'}), 200
