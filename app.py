from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

from apispec_docs import get_apispec
from database.engine import create_tables
from middleware import db_session_middleware
from routers import (create_task, delete_tasks, get_tasks, get_tasksID,
                     update_tasks)

# Создание экземпляра Flask приложения
app = Flask(__name__)

# Регистрация blueprint для маршрутов
app.register_blueprint(create_task.bp)
app.register_blueprint(get_tasksID.bp)
app.register_blueprint(get_tasks.bp)
app.register_blueprint(update_tasks.bp)
app.register_blueprint(delete_tasks.bp)

# Подключение middleware для работы с сессией базы данных
db_session_middleware(app)

create_tables()


# Маршрут для доступа к спецификации Swagger
@app.route("/swagger")
def swagger_spec():
    spec = get_apispec(app).to_dict()
    return jsonify(spec)


SWAGGER_URL = "/docs"
API_URL = "/swagger"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "Tasks API"}
)

app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == "__main__":
    app.run(debug=True)
