"""
constants to Academy Clover Kingdom
constants Clover Kingdom
author: Miguel Herize
mail: migherize@gmail.com
"""
import os
from dotenv import load_dotenv

# Cargar .env
load_dotenv()

# Leer variables de entorno
USERDB = os.getenv("userDB")
PASSWORDDB = os.getenv("passwordDB")
NAME_SERVICEDB = os.getenv("name_serviceDB")
NAMEDB = os.getenv("nameBD")
PORT = os.getenv("port")

# Constantes

list_affinity = ["Oscuridad", "Luz", "Fuego", "Agua", "Viento", "Tierra"]
dict_example = {
    "name": "Miguel",
    "surname": "Herize",
    "id": "migher25",
    "old": 25,
    "magical_affinity": "Oscuridad",
}
