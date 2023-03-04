"""
test de FastApi Academy Clover Kingdom
test de FastApi realizado con pytest para los endpoint.
author: Miguel Herize
mail: migherize@gmail.com
"""
from fastapi import status
from fastapi.testclient import TestClient
from app import main
from app.schemas.schemas import Admission
from app.utils.constants import Tupla_grimorios

# headers
cabeceras_endpoint = {"accept": "application/json", "Content-Type": "application/json"}

# constanst test

application_test = {
    "name": "Test",
    "surname": "Prueba",
    "id": "id3",
    "old": 10,
    "magical_affinity": "Oscuridad",
}


client = TestClient(app=main.app)


def test_home_page():
    """
    Test de prueba a la pagina de inicio de FastApi
    """
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "page": "home",
        "Version": "1.0",
        "Update Date": "March 04 2023",
    }


def test_application_for_admission():
    response = client.post(
        "/queries/send-admission",
        headers=cabeceras_endpoint,
        json=application_test,
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "name": response.json()["name"],
        "magical_affinity": response.json()["magical_affinity"],
        "grimorio": response.json()["grimorio"],
        "status": response.json()["status"],
    }


def test_update_admission():
    response = client.put(
        "/queries/update-admission",
        headers=cabeceras_endpoint,
        json=application_test,
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "Academia": f" Solicitud {application_test['id']} actualiza."
    }


def test_update_status_admission():
    response = client.put(
        f"/queries/update-status-admission/{application_test['id']}",
        headers=cabeceras_endpoint,
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "Academia": f"Solicitud {application_test['id']} estatus actualizado a Acceptado"
    }


def test_read_all_application():
    response = client.get(
        "/queries/all-request-read-all-application",
        headers=cabeceras_endpoint,
    )
    assert response.status_code == status.HTTP_200_OK


def test_read_assing_grimoire():
    response = client.get(
        f"/queries/read-assing-grimoire/{application_test['id']}",
        headers=cabeceras_endpoint,
    )
    assert response.status_code == status.HTTP_200_OK
    if Tupla_grimorios[0][0] in response.json():
        assert response.json() == {
            "Academia": f"La Solicitud {application_test['id']} tiene grimorio {Tupla_grimorios[0][0]}, {Tupla_grimorios[0][1]}."
        }
    elif Tupla_grimorios[1][0] in response.json():
        assert response.json() == {
            "Academia": f"La Solicitud {application_test['id']} tiene grimorio {Tupla_grimorios[1][0]}, {Tupla_grimorios[1][1]}."
        }
    elif Tupla_grimorios[2][0] in response.json():
        assert response.json() == {
            "Academia": f"La Solicitud {application_test['id']} tiene grimorio {Tupla_grimorios[2][0]}, {Tupla_grimorios[2][1]}."
        }
    elif Tupla_grimorios[3][0] in response.json():
        assert response.json() == {
            "Academia": f"La Solicitud {application_test['id']} tiene grimorio {Tupla_grimorios[3][0]}, {Tupla_grimorios[3][1]}."
        }
    elif Tupla_grimorios[4][0] in response.json():
        assert response.json() == {
            "Academia": f"La Solicitud {application_test['id']} tiene grimorio {Tupla_grimorios[4][0]}, {Tupla_grimorios[4][1]}."
        }


def test_delete_admission():
    response = client.delete(
        f"/queries/delete/{application_test['id']}",
        headers=cabeceras_endpoint,
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "Academia": f"Solicitud {application_test['id']} eliminada."
    }
