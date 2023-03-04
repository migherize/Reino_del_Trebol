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


def search_and_verify(db_conn: Session, user_id: str) -> list:
    """
    funcion para buscar la solicitud de registro y validarla.

    Args:
        db_conn (Session): Parametro de sesion base de datos.
        user_id (str): id de solicitud para buscar en base de datos.

    Returns:
        item: una lista de objeto del modelo Applicant.
    """
    item = (
        db_conn.query(models_db.Applicant)
        .filter(models_db.Applicant.id == user_id)
        .first()
    )
    if item is None:
        raise HTTPException(status_code=404, detail="Id no encontrado")

    return item


def update_user(db_conn: Session, user: schemas.Admission) -> list:
    """
    Actualizar la solicitud de registro.

    Args:
        db_conn (Session): Parametro de sesion base de datos.
        user (schemas.Admission): objeto de tipo admission para actualizar el item en la base de datos.

    Returns:
        item: una lista de objeto del modelo Applicant.
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


def create_user(
    db_conn: Session, user: schemas.Admission, grimorio: str
) -> models_db.Applicant:
    """
    Crea un estudiante en la db Academy

    Args:
        db_conn (Session): Parametro de sesion base de datos.
        user (schemas.Admission): objeto de tipo admission para crear el item en la base de datos.
        grimorio (str): string para grimorio del item en la base de datos.

    Returns:
        user_aplicant: un objeto del modelo Applicant.
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


def update_status(db_conn: Session, user_id: str) -> list:
    """
    Actualizar el estatus de la solicitud de registro.

    Args:
        db_conn (Session): Parametro de sesion base de datos.
        user_id (str): id de solicitud para buscar en la base de datos.

    Returns:
        item: una lista de objeto del modelo Applicant.
    """
    item = search_and_verify(db_conn, user_id)
    item.status = constants.STATUS_UPDATE
    db_conn.add(item)
    db_conn.commit()
    db_conn.refresh(item)
    return item


def select_grimorio(db_conn: Session, user_id: str) -> list:
    """
    Consultar grimorio de una solicitud de registro.

    Args:
        db_conn (Session): Parametro de sesion base de datos.
        user_id (str): id de solicitud para buscar en la base de datos.

    Returns:
        item: una lista de objeto del modelo Applicant.
    """
    item = search_and_verify(db_conn, user_id)
    return item


def delete_admission(db_conn: Session, user_id: str) -> list:
    """
    Eliminar una solicitud de registro.

    Args:
        db_conn (Session): Parametro de sesion base de datos.
        user_id (str): id de solicitud para eliminar en la base de datos.

    Returns:
        item: una lista de objeto del modelo Applicant.
    """
    item = search_and_verify(db_conn, user_id)
    db_conn.delete(item)
    db_conn.commit()
    return item
