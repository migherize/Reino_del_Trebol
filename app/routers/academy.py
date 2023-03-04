"""
Endpoint Academy Clover Kingdom
Router Clover Kingdom
author: Miguel Herize
mail: migherize@gmail.com
"""

import random
import logging
import json
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import schemas
from app.models import models_db, database, crud
import app.utils.constants as constants

logging.basicConfig(
    filename=constants.PATH_BITACORA,
    encoding="utf-8",
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
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

    Args:

        User (dict): Un Diccionario con datos en formato JSON.
            {
                "name": "string",
                "surname": "string",
                "id": "string",
                "old": "int",
                "magical_affinity": "string",
            }

    Valores validos:
    * id = string alphanumerico máximo 10 caracteres.
    * name = string solo letras a-z máximo 20 caracteres.
    * surname = string solo letras a-z máximo 20 caracteres.
    * old = entero de 2 digitos.
    * magical_affinity = "Oscuridad", "Luz", "Fuego", "Agua", "Viento", "Tierra".

    Returns:
        dict: Diccionario con la solicitud de registro.

        User (dict): Un Diccionario con datos en formato JSON.
            {
                "name": "string",
                "magical_affinity": "string",
                "grimorio": "string",
                "status": "string",
            }
    """
    logging.info("### Solicitud de registro ###")
    fullname = f"{user.name} {user.surname}"
    logging.info("Nombre: %s", fullname)

    # Assing grimorio
    random_tuple = random.choice(constants.Tupla_grimorios)
    logging.info("Grimorio random: %s , %s", random_tuple[0], random_tuple[1])
    grimorio = f"{random_tuple[0]}, {random_tuple[1]}"

    try:
        db_item = crud.create_user(db_conn, user, grimorio)
        logging.info("db: %s", db_item)

        result = schemas.ResultJson(
            name=fullname,
            magical_affinity=str(db_item.magical_affinity),
            grimorio=db_item.grimorio,
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
    la actualizacion de la solicitud de registro a la academia.

    Args:

        User (dict): Un Diccionario con datos en formato JSON.
            {
                "name": "string",
                "surname": "string",
                "id": "string",
                "old": "int",
                "magical_affinity": "string",
            }

    Valores validos:
    * id = string alphanumerico máximo 10 caracteres.
    * name = string solo letras a-z máximo 20 caracteres.
    * surname = string solo letras a-z máximo 20 caracteres.
    * old = entero de 2 digitos.
    * magical_affinity = "Oscuridad", "Luz", "Fuego", "Agua", "Viento", "Tierra".

    Returns:
        string: mensaje de objeto actualizado.

    """
    logging.info("### Actualizar una solicitud de registro ###")
    db_item = crud.update_user(db_conn, user)

    logging.info("id: %s actualizada", db_item.id)

    return {"Academia": f" Solicitud {db_item.id} actualiza."}


@clover_kingdom.put("/update-status-admission/{user_id}")
def update_status_admission(
    user_id: str, db_conn: Session = Depends(database.get_db)
) -> dict:
    """Actualizar estatus de solicitud.

    Actualiza el estatus de la solicitud del registro a la academia.
    estatus posibles: Pendiente y Acceptado

    Args:
        user_id (string): identicador unico de la solicitud del registro

    Valores validos:
    * id = string alphanumerico máximo 10 caracteres.

    Returns:
        string: mensaje de solicitud actualizada.
    """
    logging.info("### Actualizar estatus de solicitud de registro ###")
    db_item = crud.update_status(db_conn, user_id)

    logging.info("id: %s", db_item.id)
    logging.info("Status: %s", db_item.status)

    if db_item.status:
        return {
            "Academia": f"Solicitud {db_item.id} estatus actualizado a {constants.STATUS_ACCEPTED}"
        }


@clover_kingdom.get("/all-request-read-all-application")
def read_all_application(db_conn: Session = Depends(database.get_db)) -> list:
    """Consultar todas las solicitudes.

    Funciona para traer todas las solicitudes de registro en la base de datos.

    Returns:
        list: Un lista con todos las solicitudes de registro de la academia.
    """
    logging.info("### Ver todas las solicitudes de registro ###")
    data = db_conn.query(models_db.Applicant).all()
    logging.info("cantidad: %s", len(data))

    return data


@clover_kingdom.get("/read-assing-grimoire/{user_id}")
def read_assing_grimoire(
    user_id: str, db_conn: Session = Depends(database.get_db)
) -> dict:
    """Consultar asignaciones de Grimorios.

    Ver asignacion de grimorio de uuna solicitud de ingreso.

    Args:
        user_id (string): identicador unico de la solicitud del registro.

    Valores validos:
    * id = string alphanumerico máximo 10 caracteres.

    Returns:
        string: mensaje de grimorio asignado a la solicitud.
    """
    logging.info("### Consulta de Grimorio ###")
    db_item = crud.select_grimorio(db_conn, user_id)
    logging.info("id: %s", db_item.id)
    logging.info("Grimorio: %s", db_item.grimorio)

    if db_item:
        return {
            "Academia": f"La solicitud {db_item.id} tiene grimorio {db_item.grimorio}."
        }


@clover_kingdom.delete("/delete/{user_id}")
def delete_admission(user_id: str, db_conn: Session = Depends(database.get_db)) -> dict:
    """Eliminar solicitud de ingreso.

    Borrar la solicitud de ingreso de un estudiante.

    Args:
        user_id (string): identicador unico de la solicitud del registro.

    Valores validos:
    * id = string alphanumerico máximo 10 caracteres.

    Returns:
        string: mensaje de solicitud id eliminada.
    """
    logging.info("### Eliminar Solicitud de ingreso ###")
    db_item = crud.delete_admission(db_conn, user_id)
    logging.info("Eliminado: %s", db_item.id)

    if db_item:
        return {"Academia": f"Solicitud {db_item.id} eliminada."}
