from flask import Flask
from database.engine import create_tables
from routers import create_task, get_tasksID, get_tasks, update_tasks, delete_tasks
from middleware import db_session_middleware

app = Flask(__name__)


app.register_blueprint(create_task.bp)
app.register_blueprint(get_tasksID.bp)
app.register_blueprint(get_tasks.bp)
app.register_blueprint(update_tasks.bp)
app.register_blueprint(delete_tasks.bp)

db_session_middleware(app)

create_tables()

if __name__ == '__main__':
    app.run(debug=True)
