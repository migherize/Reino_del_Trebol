"""
Endpoint Academy Clover Kingdom
Router Clover Kingdom
author: Miguel Herize
mail: migherize@gmail.com
"""

import logging
from fastapi import APIRouter
from models import user_model

clover_kingdom = APIRouter(
    prefix="/queries",
    tags=["Academia de Magia"],
    responses={404: {"status": "disconnected"}},
)


# Endpoint clover_kingdom
@clover_kingdom.post("/send-admission")
def application_for_admission(user: user_model.Admission):
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
    result = {"nombre_completo": fullname, "edad": user.old}
    return result


@clover_kingdom.put("/update-admission")
def update_admission():
    """Actualizar solicitud de ingreso.

    Actualiza la solicitud de ingreso a la academia de magia, es decir,
    la actualizacion del registro del estudiante a la academia.

    """
    return {"Application": "Update Successful"}


@clover_kingdom.put("/update-status-admission")
def update_status_admission():
    """Actualizar estatus de solicitud.

    Actualiza el estatus de la solicitud del estudiante a la academia.

    """
    return {"Application": "Update Successful"}


@clover_kingdom.get("/all-request-read-all-application")
def read_all_application():
    """Consultar todas las solicitudes.

    Funciona para traer todos las solicitudes de los estudiantes a registrar.

    """
    return {"Application": "All Application"}


@clover_kingdom.get("/read-assing-grimoire")
def read_assing_grimoire():
    """Consultar asignaciones de Grimorios.

    Ver asignacion de grimorios de un estudiante.

    """
    return {"Application": "Assing Grimoire"}


@clover_kingdom.delete("/delete")
def delete_admission():
    """Eliminar solicitud de ingreso.

    Borrar una solicitud de ingreso de un estudiante.

    """
    return {"Application": "Delete student"}
