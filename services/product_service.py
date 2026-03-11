from sqlalchemy.orm import Session
from fastapi import HTTPException
from repositories import product_repository
from schemas.pydantic_dtos import ProductCreate

def create_new_product(db: Session, product_data: ProductCreate):
    # Llamamos el repositorio para guarddar en la DB
    return product_repository.create_product_in_db(
        db=db,
        name=product_data.name,
        price=product_data.price,
        category=product_data.category
    )