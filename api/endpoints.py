from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from models.domain import User, Product
from schemas.pydantic_dtos import UserCreate, UserResponse, ProductCreate, ProductResponse

# creamos el enrutador
router = APIRouter()

# --- ENDPOINT DE USUARIOS ---
@router.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # 1. Transformamos el esquema de Pydantic al modelo de SQLAlchemy
    db_user = User(email=user.email, name=user.name)

    # 2. Guardamos en la base de datos
    db.add(db_user)
    db.commit()
    db.refresh(db_user) # obtenemos el ID y el created_at

    return db_user

# --- ENDPOINT DE PRODUCTOS ---
@router.post("/products/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product =Product(name=product.name, price=product.price, category=product.category)

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product
