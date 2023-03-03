# Reino_del_Trebol

Api construida con fastApi para simulador el mundo del Reino del Trebol, donde se requiere diseñar un sistema para la academia de magia.

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

## Funcionalidades (Endpoint)

1. application_for_admission
2. update_admission
3. update_status_admission
4. read_all_application
5. read_assing_grimoire
6. delete_admission

## Requisitos
1. Python 3.10.7
2. FastApi 0.92.0
3. pydantic 1.10.5
4. SQLAlchemy 2.0.4
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

## Uso
1. Ejecutar el proyecto

    ```
    uvicorn app.main:app --reload
    ```
2. Acceder a http://127.0.0.1:8000/docs

## Contribución
1. Fork del repositorio
2. Crear una rama

    ```
    git checkout -b feature/nueva-funcionalidad
    ```