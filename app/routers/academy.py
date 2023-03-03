"""
Endpoint Academy Clover Kingdom
Router Clover Kingdom
author: Miguel Herize
mail: migherize@gmail.com
"""

import logging
import json
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import schemas
from app.models import models_db, database, crud
import app.utils.constants as constants

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

clover_kingdom = APIRouter(
    prefix="/queries",
    tags=["Academia de Magia"],
    responses={404: {"status": "disconnected"}},
)


# Endpoint clover_kingdom
@clover_kingdom.post("/send-admission")
def application_for_admission(
    user: schemas.Admission, db_conn: Session = Depends(database.get_db)
) -> dict:
    """
    Endpoint que envia la solicitud de ingreso a la academia de magia.

    Envia la solicitud de ingreso a la academia de magia, es decir,
    el registro del estudiante a la academia.

    Parámetros:

        user_application (dict): Un Diccionario con datos en formato JSON.
            {
                "name": "string",
                "surname": "string",
                "id": "string",
                "old": "int",
                "magical_affinity": "string",
            }
        User (dict): Un Diccionario con datos en formato JSON.
            {
                "name": "string",
                "surname": "string",
                "id": "string",
                "old": "int",
                "magical_affinity": "string",
            }

    Retorna:

        str: Un string con el estatus del registro del estudiante.
    """
    fullname = f"{user.name} {user.surname}"
    logging.info("Nombre: %s", fullname)

    try:
        db_item = crud.create_user(db_conn, user)
        logging.info("db: %s", db_item)

        result = schemas.ResultJson(
            name=fullname,
            magical_affinity=str(user.magical_affinity),
            status=constants.STATUS_PENDIND,
        )
        my_json = result.show_json()
        return my_json

    except Exception as exc:
        raise HTTPException(
            status_code=400,
            detail=json.dumps({"error": "Ocurrio un error. ID Aplicante ya existe."}),
        ) from exc


@clover_kingdom.put("/update-admission/")
def update_admission(
    user: schemas.Admission, db_conn: Session = Depends(database.get_db)
) -> dict:
    """Actualizar solicitud de ingreso.

    Actualiza la solicitud de ingreso a la academia de magia, es decir,
    la actualizacion del registro del estudiante a la academia.

    """
    db_item = crud.update_user(db_conn, user)

    logging.info("Nombre: %s", db_item.id)

    return {"Academia": f" Solicitud {db_item.id} actualiza."}


@clover_kingdom.put("/update-status-admission/{user_id}")
def update_status_admission(
    user_id: str, db_conn: Session = Depends(database.get_db)
) -> dict:
    """Actualizar estatus de solicitud.

    Actualiza el estatus de la solicitud del estudiante a la academia.

    """
    db_item = crud.update_status(db_conn, user_id)

    logging.info("Status: %s", db_item.status)

    if db_item.status:
        return {
            "Academia": f"Estudiante {db_item.id} estatu actualizado a {constants.STATUS_ACCEPTED}"
        }


@clover_kingdom.get("/all-request-read-all-application")
def read_all_application(db_conn: Session = Depends(database.get_db)) -> list:
    """Consultar todas las solicitudes.

    Funciona para traer todas las solicitudes de registro.

    Retorna:

        list: Un lista con todos los estudiantes de la academia.
    """
    data = db_conn.query(models_db.Applicant).all()

    return data


@clover_kingdom.get("/read-assing-grimoire")
def read_assing_grimoire():
    """Consultar asignaciones de Grimorios.

    Ver asignacion de grimorios de un estudiante.

    """
    return {"Application": "Assing Grimoire"}


@clover_kingdom.delete("/delete/{user_id}")
def delete_admission(user_id: str, db_conn: Session = Depends(database.get_db)) -> dict:
    """Eliminar solicitud de ingreso.

    Borrar una solicitud de ingreso de un estudiante.

    """
    db_item = crud.delete_admission(db_conn, user_id)
    logging.info("Eliminado: %s", db_item.id)

    if db_item:
        return {"Academia": f"Solicitud {db_item.id} eliminada."}
