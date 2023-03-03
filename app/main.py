"""
main Academy Clover Kingdom
api Clover Kingdom
author: Miguel Herize
mail: migherize@gmail.com
"""
# main.py
from fastapi import FastAPI
from app.routers import academy

app = FastAPI()

# Endpoint Academy
app.include_router(academy.clover_kingdom)
