from flask import Blueprint, jsonify, g
from database.crud import orm_get_all_tasks
from database.engine import SessionLocal
from schemas import TaskSchema

bp = Blueprint('get_tasks', __name__)
task_schema = TaskSchema(many=True)

@bp.route('/tasks', methods=['GET'])
def get_tasks():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = SessionLocal()

    tasks = orm_get_all_tasks(db)
    response_data = task_schema.dump(tasks)
    return jsonify(response_data), 200
