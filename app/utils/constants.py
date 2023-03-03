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
DB = os.getenv("DB")
USERDB = os.getenv("userDB")
PASSWORDDB = os.getenv("passwordDB")
NAME_SERVICEDB = os.getenv("name_serviceDB")
NAMEDB = os.getenv("nameBD")
PORT = os.getenv("port")

# Constantes
STATUS_INPUT = False
list_grimorios = [
    ("Sinceridad", "Trébol de 1 hoja"),
    ("Esperanza", "Trébol de 2 hojas"),
    ("Amor", "Trébol de 3 hojas"),
    ("Buena Fortuna", "Trébol de 4 hojas"),
    ("Desesperación", "Trébol de 5 hojas"),
]
list_affinity = ["Oscuridad", "Luz", "Fuego", "Agua", "Viento", "Tierra"]
dict_example = {
    "name": "Miguel",
    "surname": "Herize",
    "id": "migher25",
    "old": 25,
    "magical_affinity": "Oscuridad",
}
