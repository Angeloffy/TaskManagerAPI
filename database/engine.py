from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.cfg import MySQL_cfg as cfg
from database.models import Base

connect_string = f'mysql+pymysql://{cfg["user"]}:{cfg["password"]}@{cfg["host"]}:{cfg["port"]}/{cfg["database"]}'
engine = create_engine(connect_string, echo=False)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_tables():
    Base.metadata.create_all(bind=engine)
