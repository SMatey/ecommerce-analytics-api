from fastapi import FastAPI
from core.database import engine, Base
from models import domain

from api.endpoints import router as api_router

# Traducimos las clases de python a codigo SQL (creamos las tablas si no estan creadas)
Base.metadata.create_all(bind=engine)

# Inicializamos la aplicacion de FastApi
app = FastAPI(title="E-commerce Analytics API")

# Agregamos el router a la aplicacion principal
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"mensaje": "La API y la Base de Datos estan conectadas y las tablas fueron creadas!"}