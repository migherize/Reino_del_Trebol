"""
Create, Read, Update, and Delete to database Academy.
crud Clover Kingdom
author: Miguel Herize
mail: migherize@gmail.com
"""
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models import models_db
from app.schemas import schemas
import app.utils.constants as constants


def search_and_verify(db_conn: Session, user_id: str):
    """
    funcion para buscar la solicitud de registro y validarla.
    """
    item = (
        db_conn.query(models_db.Applicant)
        .filter(models_db.Applicant.id == user_id)
        .first()
    )
    if item is None:
        raise HTTPException(status_code=404, detail="Id no encontrado")

    return item


def update_user(db_conn: Session, user: schemas.Admission):
    """
    Actualizar la solicitud de registro.
    """
    item = search_and_verify(db_conn, user.id)
    item.name = user.name
    item.surname = user.surname
    item.old = user.old
    item.magical_affinity = user.magical_affinity

    db_conn.add(item)
    db_conn.commit()
    db_conn.refresh(item)
    return item


def create_user(db_conn: Session, user: schemas.Admission, grimorio: str):
    """
    Crea un estudiante en la db Academy
    """
    user_aplicant = models_db.Applicant(
        name=user.name,
        surname=user.surname,
        id=user.id,
        old=user.old,
        magical_affinity=user.magical_affinity,
        grimorio=grimorio,
        status=constants.STATUS_INPUT,
    )

    db_conn.add(user_aplicant)
    db_conn.commit()

    return user_aplicant


def update_status(db_conn: Session, user_id: str):
    """
    Actualizar el estatus de la solicitud de registro.
    """
    item = search_and_verify(db_conn, user_id)
    item.status = constants.STATUS_UPDATE
    db_conn.add(item)
    db_conn.commit()
    db_conn.refresh(item)
    return item


def select_grimorio(db_conn: Session, user_id: str):
    """
    Consultar grimorio de una solicitud de registro.
    """
    item = search_and_verify(db_conn, user_id)
    return item


def delete_admission(db_conn: Session, user_id: str):
    """
    Eliminar una solicitud de registro.
    """
    item = search_and_verify(db_conn, user_id)
    db_conn.delete(item)
    db_conn.commit()
    return item
