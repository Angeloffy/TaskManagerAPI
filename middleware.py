from flask import g

from database.engine import SessionLocal


def db_session_middleware(app):
    @app.before_request
    def create_session():
        g.db_session = SessionLocal()

    @app.teardown_request
    def close_session(exception=None):
        session = g.pop("db_session", None)
        if session is not None:
            if exception is None:
                session.commit()
            else:
                session.rollback()
            session.close()
