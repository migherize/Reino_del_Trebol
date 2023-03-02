"""
class pydantic to models Academy Clover Kingdom
models Clover Kingdom
author: Miguel Herize
mail: migherize@gmail.com
"""

import re
import pydantic


class Admission(pydantic.BaseModel):
    """Solicitud de ingreso.

    Objeto para solicitar la admission a la academia.

    """

    name: str
    surname: str
    id: str
    old: int
    magical_affinity: str

    @pydantic.validator("name", "surname")
    # pylint: disable=no-self-argument
    def name_not_number_and_size_twenty(cls, v):
        """
        Nombre debe ser solo letras y maximo 20 caracteres.
        """
        if not re.match("^[^0-9]+$", v) or len(v) > 20:
            raise ValueError("El campo debe contener maximo 20 caracteres solo letras.")
        return v

    @pydantic.validator("id")
    # pylint: disable=no-self-argument
    def id_alphanumeric_and_size_ten(cls, v):
        """
        Identificador debe ser alphanumerico (letras y numeros) y maximo 10 caracteres.
        """
        if not re.match("^[a-zA-Z0-9]{0,10}$", v):
            raise ValueError(
                "El campo debe contener máximo 10 caracteres alfanuméricos."
            )
        return v

    @pydantic.validator("old")
    # pylint: disable=no-self-argument
    def old_only_number_and_size_two(cls, v):
        """
        Solo numeros 2 digitos (00-99)
        """
        if not re.match("^[0-9]{2}$", str(v)):
            raise ValueError("El campo debe contener solo números de 2 dígitos")
        return v
