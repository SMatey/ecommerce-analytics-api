from fastapi import FastAPI
from core.database import engine, Base
from models import domain

# Traducimos las clases de python a codigo SQL
Base.metadata.create_all(bind=engine)

# Inicializamos la aplicacion de FastApi
app = FastAPI(title="E-commerce Analytics API")

@app.get("/")
def read_root():
    return {"mensaje": "La API y la Base de Datos estan conectadas y las tablas fueron creadas!"}