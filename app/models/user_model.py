"""
class pydantic to models Academy Clover Kingdom
models Clover Kingdom
author: Miguel Herize
mail: migherize@gmail.com
"""

import re
from typing import List, Tuple

# pylint: disable=no-name-in-module
from pydantic import BaseModel, validator

import app.utils.constants as constants


class Grimorios(BaseModel):
    """
    Clase que representa los niveles de Grimorios

    Niveles de Grimorios:
        ▪ Sinceridad - Trébol de 1 hoja.
        ▪ Esperanza - Trébol de 2 hojas.
        ▪ Amor - Trébol de 3 hojas.
        ▪ Buena Fortuna - Trébol de 4 hojas.
        ▪ Desesperación - Trébol de 5 hojas.

    Atributos:
        ▪ Lista [Tuplas[]]: una lista de tuplas con los Niveles de Grimorios.

    """

    tipos: List[Tuple[str, str]]


class Admission(BaseModel):
    """
    Clase que representa uan solicitud de ingreso para la admission a la academia.

    Atributos:
        ▪ Nombre (solo letras, máximo 20 caracteres).
        ▪ Apellido (solo letras, máximo 20 caracteres).
        ▪ Identificación (números y letras, máximo 10 caracteres).
        ▪ Edad (solo números, 2 dígitos).
        ▪ Afinidad Mágica (mencionadas anteriormente).
    """

    name: str
    surname: str
    id: str
    old: int
    magical_affinity: str

    class Config:
        """
        Ejemplo para el modelo de Admission y para swagger FastApi
        """

        schema_extra = {"example": constants.dict_example}

    @validator("name", "surname")
    # pylint: disable=no-self-argument
    def name_not_number_and_size_twenty(cls, value: str) -> str:
        """
        Nombre debe ser solo letras y maximo 20 caracteres.
        """
        if not re.match("^[^0-9]+$", value) or len(value) > 20:
            raise ValueError("El campo debe contener maximo 20 caracteres solo letras.")
        return value

    @validator("id")
    # pylint: disable=no-self-argument
    def id_alphanumeric_and_size_ten(cls, value: str) -> str:
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
    def old_only_number_and_size_two(cls, value: int) -> int:
        """
        Solo numeros 2 digitos (00-99)
        """
        if not re.match("^[0-9]{2}$", str(value)):
            raise ValueError("El campo debe contener solo números de 2 dígitos")
        return value

    @validator("magical_affinity")
    # pylint: disable=no-self-argument
    def magical_affinity_verify_value(cls, value: str) -> str:
        """Validar Afinidad magica

        Solo puede contener los siguientes valores:
            ▪ Oscuridad
            ▪ Luz
            ▪ Fuego
            ▪ Agua
            ▪ Viento
            ▪ Tierra
        """
        affinity = set(constants.list_affinity)
        if not value in affinity:
            raise ValueError(f"El valor {value} no está permitido")
        return value
