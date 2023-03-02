"""
class pydantic to models Academy Clover Kingdom
models Clover Kingdom
author: Miguel Herize
mail: migherize@gmail.com
"""

import re

# pylint: disable=no-name-in-module
from pydantic import BaseModel, validator


class Admission(BaseModel):
    """Solicitud de ingreso.

    Objeto para solicitar la admission a la academia.

    """

    name: str
    surname: str
    id: str
    old: int
    magical_affinity: str

    @validator("name", "surname")
    # pylint: disable=no-self-argument
    def name_not_number_and_size_twenty(cls, value):
        """
        Nombre debe ser solo letras y maximo 20 caracteres.
        """
        if not re.match("^[^0-9]+$", value) or len(value) > 20:
            raise ValueError("El campo debe contener maximo 20 caracteres solo letras.")
        return value

    @validator("id")
    # pylint: disable=no-self-argument
    def id_alphanumeric_and_size_ten(cls, value):
        """
        Identificador debe ser alphanumerico (letras y numeros) y maximo 10 caracteres.
        """
        if not re.match("^[a-zA-Z0-9]{0,10}$", value):
            raise ValueError(
                "El campo debe contener máximo 10 caracteres alfanuméricos."
            )
        return value

    @validator("old")
    # pylint: disable=no-self-argument
    def old_only_number_and_size_two(cls, value):
        """
        Solo numeros 2 digitos (00-99)
        """
        if not re.match("^[0-9]{2}$", str(value)):
            raise ValueError("El campo debe contener solo números de 2 dígitos")
        return value

    @validator("magical_affinity")
    # pylint: disable=no-self-argument
    def magical_affinity_verify_value(cls, value):
        """
        Solo puede contener los siguientes valores:
            ▪ Oscuridad
            ▪ Luz
            ▪ Fuego
            ▪ Agua
            ▪ Viento
            ▪ Tierra
        """
        affinity = set(["Oscuridad", "Luz", "Fuego", "Agua", "Viento", "Tierra"])
        for valor in value:
            if valor in affinity:
                raise ValueError(f"El valor {valor} no está permitido")
        return value
