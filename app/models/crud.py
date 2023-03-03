"""
Create, Read, Update, and Delete to database Academy.
crud Clover Kingdom
author: Miguel Herize
mail: migherize@gmail.com
"""
from sqlalchemy.orm import Session
from app.models import models_db
from app.schemas import schemas
import app.utils.constants as constants


def get_user(db_conn: Session, user_id: str):
    """
    Consulta a la base de datos un usuario por su Id
    """
    return (
        db_conn.query(models_db.Applicant)
        .filter(models_db.Applicant.id == user_id)
        .first()
    )


def create_user(db_conn: Session, user: schemas.Admission):
    """
    Crea un estudiante en la db Academy
    """
    user_aplicant = models_db.Applicant(
        name=user.name,
        surname=user.surname,
        id=user.id,
        old=user.old,
        magical_affinity=user.magical_affinity,
        status=constants.STATUS_INPUT,
    )

    db_conn.add(user_aplicant)
    db_conn.commit()

    return user_aplicant
