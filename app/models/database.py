"""
database Academy Clover Kingdom
database, connection, session with sqlalchemy to Clover Kingdom
author: Miguel Herize
mail: migherize@gmail.com
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import app.utils.constants as constants

# connection to DB (orm = SQLAlchemy)
eng = (
    "mysql+pymysql://"
    + constants.USERDB
    + ":"
    + constants.PASSWORDDB
    + "@"
    + constants.NAME_SERVICEDB
    + ":"
    + constants.PORT
    + "/"
    + constants.NAMEDB
)
engine = create_engine(eng)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Crear tablas
Base.metadata.create_all(bind=engine)


def get_db():
    """
    conexion database
    """
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()
