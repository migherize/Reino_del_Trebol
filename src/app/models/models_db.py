"""
models to database Academy
models Clover Kingdom
author: Miguel Herize
mail: migherize@gmail.com
"""

from sqlalchemy import Column, Integer, String, Boolean, Tuple as SqlTuple
from app.models.database import Base


class Applicant(Base):
    """
    Tabla aplicante en la base de datos.
    """

    __tablename__ = "applicant"
    id = Column(String(10), primary_key=True)
    name = Column(String(20))
    surname = Column(String(20))
    old = Column(Integer)
    magical_affinity = Column(String(20))
    grimorio = Column(String(100))
    status = Column(Boolean, default=True)
