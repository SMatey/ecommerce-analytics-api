from sqlalchemy.orm import Session
from fastapi import HTTPException
from repositories import user_repository
from schemas.pydantic_dtos import UserCreate

def create_new_user(db: Session, user_data: UserCreate):
    # Llamamos el repositorio para guarddar en la DB
    return user_repository.create_user_in_db(
        db=db,
        email=user_data.email,
        name=user_data.name
    )