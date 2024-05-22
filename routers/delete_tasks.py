from flask import Blueprint, g, jsonify

from database.crud import orm_delete_task

bp = Blueprint("delete_task", __name__)


@bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    success = orm_delete_task(g.db_session, task_id)

    if not success:
        return jsonify({"error": "Task not found"}), 404

    return jsonify({"message": "Task successfully deleted"}), 200
