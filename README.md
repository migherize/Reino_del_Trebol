# Reino del Trebol

Api construida con fastApi para simulador el mundo del Reino del Trebol, donde se requiere diseñar un sistema para una academia de magia.

![FastApi](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)

### Ambiente: 

En el Reino del Trébol, El Rey Mago requiere diseñar un sistema para la academia de magia; este debe realizar el registro de solicitud del estudiante y la asignación aleatoria de su Grimorio. 

El nivel de estos Grimorios está categorizado por el tipo de trébol en la portada:

    * Sinceridad – Trébol de 1 hoja.
    * Esperanza – Trébol de 2 hojas.
    * Amor – Trébol de 3 hojas.
    * Buena Fortuna - Trébol de 4 hojas.
    * Desesperación – Trébol de 5 hojas.

Los estudiantes tendrán una de las siguientes afinidades de magia:

    * Oscuridad
    * Luz
    * Fuego
    * Agua
    * Viento
    * Tierra

### Instrucciones:

Para este requerimiento se requiere exponer un API Rest, construida con las herramientas
antes mencionadas.
Deben exponerse a través de Postman o Swagger los endpoints necesarios para soportar
las siguientes operaciones:

* Enviar solicitud de ingreso.
* Actualizar solicitud de ingreso.
* Actualizar estatus de solicitud.
* Consultar todas las solicitudes.
* Consultar asignaciones de Grimorios.
* Eliminar solicitud de ingreso.

Una vez aprobada la solicitud se debe realizar la auto asignación de Grimorio y de portada.
Las solicitudes de ingreso deben indicar como mínimo los siguientes datos del aspirante:

* Nombre (solo letras, máximo 20 caracteres).
* Apellido (solo letras, máximo 20 caracteres).
* Identificación (números y letras, máximo 10 caracteres).
* Edad (solo números, 2 dígitos).
* Afinidad Mágica (mencionadas anteriormente).

Al incumplir cualquiera de estos criterios automáticamente la solicitud queda rechazada y
no se debe asignar Grimorio.

## Funcionalidades

![swagger FastApi](./diagrams/swagger.png)

## Endpoint
## 1. application_for_admission (POST) 

    Endpoint que envia la solicitud de ingreso a la academia de magia.

    Envia la solicitud de ingreso a la academia de magia, es decir, el registro del estudiante a la academia.

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

    id = string alphanumerico máximo 10 caracteres.
    name = string solo letras a-z máximo 20 caracteres.
    surname = string solo letras a-z máximo 20 caracteres.
    old = entero de 2 digitos.
    magical_affinity = "Oscuridad", "Luz", "Fuego", "Agua", "Viento", "Tierra".
    
    Returns: dict: Diccionario con la solicitud de registro.

    User (dict): Un Diccionario con datos en formato JSON.
        {
            "name": "string",
            "magical_affinity": "string",
            "grimorio": "string",
            "status": "string",
        }

## 2. update_admission (PUT)

    Actualizar solicitud de ingreso.

    Actualiza la solicitud de ingreso a la academia de magia, es decir, la actualizacion de la solicitud de registro a la academia.

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

    id = string alphanumerico máximo 10 caracteres.
    name = string solo letras a-z máximo 20 caracteres.
    surname = string solo letras a-z máximo 20 caracteres.
    old = entero de 2 digitos.
    magical_affinity = "Oscuridad", "Luz", "Fuego", "Agua", "Viento", "Tierra".

    Returns: string: mensaje de objeto actualizado.

## 3. update_status_admission (PUT)

    Actualizar estatus de solicitud.

    Actualiza el estatus de la solicitud del registro a la academia. estatus posibles: Pendiente y Acceptado

    Args: user_id (string): identicador unico de la solicitud del registro

    Valores validos:

    id = string alphanumerico máximo 10 caracteres.
    Returns: string: mensaje de solicitud actualizada.

## 4. read_all_application (GET)
    Consultar todas las solicitudes.

    Funciona para traer todas las solicitudes de registro en la base de datos.

    Returns: list: Un lista con todos las solicitudes de registro de la academia.


## 5. read_assing_grimoire (GET)

    Consultar asignaciones de Grimorios.

    Ver asignacion de grimorio de uuna solicitud de ingreso.

    Args: user_id (string): identicador unico de la solicitud del registro.

    Valores validos:

    id = string alphanumerico máximo 10 caracteres.
    Returns: string: mensaje de grimorio asignado a la solicitud.

## 6. delete_admission (DELETE)

    Eliminar solicitud de ingreso.

    Borrar la solicitud de ingreso de un estudiante.

    Args: user_id (string): identicador unico de la solicitud del registro.

    Valores validos:

    id = string alphanumerico máximo 10 caracteres.
    Returns: string: mensaje de solicitud id eliminada.


## Requisitos
1. Python 3.10.7
2. FastApi 0.92.0
3. Pydantic 1.10.5
4. SQLAlchemy 2.0.4

5. IDE: Visual Studio 2022 / Visual Code / PyCharm
6. Base de datos: SQL / MySQL / Postgresql / MongoDB / CouchDB / Redis / MariaDB
7. Postman (para pruebas).
## Instalación
1. Clonar el repositorio
    ```
    git clone https://github.com/migherize/Reino_del_Trebol.git

    ```
2. Instalar dependencias
    ```
    cd Reino_del_Trebol
    pipenv install
    pipenv install -r requirements.txt
    ```

3. Crear Base de datos

    Para crear la base de datos puedes utilizar cualquier motor de base de datos (SQL / MySQL / Postgresql / MongoDB / CouchDB / Redis / MariaDB) o cualquier herramienta visual (MysqlWorbench o PgAdmin), solo debemos crear la base de datos y configurar nuestras variables de entorno, gracias a que create_engine de SQLAlchemy nos facilita una conexion segura utilizando la siguientes plantillas de ejemplo:
    ```
    postgresql://<usuario>:<contraseña>@<host>:<puerto>/<base_de_datos>

    mysql+pymysql://<usuario>:<contraseña>@<host>:<puerto>/<base_de_datos>
    ```
    Para la cual esta configurado la siguientes variables de entorno.

4. Variables de entorno para conec
    - `name_serviceDB`: El host de la base de datos utilizada por la aplicación.
    - `DB`: El puerto de la base de datos utilizada por la aplicación.
    - `userDB`: Usuario de base de datos utilizada por la aplicación.
    - `passwordDB`: Contraseña de base de datos utilizada por la aplicación.
    - `nameBD`: Nombre de la base de datos utilizada por la aplicación.
    - `port`: El puerto de la base de datos utilizada por la aplicación.
    
    
    #### Crear archivo .env
    ```
    touch .env
    ```
    #### Ejemplo .env
    ```
    DB = "mysql+pymysql"
    userDB="root"
    passwordDB="password"
    name_serviceDB="localhost"
    nameBD="name_database"
    port="3306"
    ```
    #### Formato de conexion de ejemplo
    ```
    # create_engine

    postgresql://<usuario>:<contraseña>@<host>:<puerto>/<base_de_datos>

    ```
## Uso
1. Ejecutar el proyecto

    ```
    uvicorn app.main:app --reload
    ```
2. Acceder a http://127.0.0.1:8000/docs
2. Documentacion mas detallada http://127.0.0.1:8000/redoc

## Contribución
1. Fork del repositorio
2. Crear una rama

    ```
    git checkout -b feature/nueva-funcionalidad
    ```