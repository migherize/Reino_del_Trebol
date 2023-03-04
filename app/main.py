"""
main Academy Clover Kingdom
api Clover Kingdom
author: Miguel Herize
mail: migherize@gmail.com
"""
# main.py
from fastapi import FastAPI
from app.routers import academy
from app.models.database import Base, engine

# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home_page():
    """
    Clasica pagina de inicio de Fastapi
    """
    return {"page": "home", "Version": "1.0", "Update Date": "March 04 2023"}


# Endpoint Academy
app.include_router(academy.clover_kingdom)
