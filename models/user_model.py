"""
class pydantic to models Academy Clover Kingdom
models Clover Kingdom
author: Miguel Herize
mail: migherize@gmail.com
"""

from pydantic import BaseModel, validator
import re

class Grimorios(BaseModel):
    tye_grimorios: str

class MagicalAffinity(BaseModel):
    type_affinity: str

class Admission(BaseModel):
    """ Solicitud de ingreso.
    
    Objeto para solicitar la admission a la academia.
    
    """
    name: str
    surname: str
    id: int
    old: int
    magical_affinity: str

    @validator('name')
    # pylint: disable=no-self-argument
    def name_not_number_and_size_twenty(cls, v):
        """
        Nombre debe ser solo letras y maximo 20 caracteres.
        """
        if not re.match("^[^0-9]+$", v) or len(v) > 20:
            raise ValueError('Este campo no puede contener números y tamaño maximo 20')
        return v
