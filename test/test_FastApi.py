"""
test de FastApi Academy Clover Kingdom
test de FastApi realizado con pytest para los endpoint.
author: Miguel Herize
mail: migherize@gmail.com
"""
from fastapi import status
from fastapi.testclient import TestClient
from app import main

# headers
cabeceras_endpoint = {"accept": "application/json", "Content-Type": "application/json"}

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
