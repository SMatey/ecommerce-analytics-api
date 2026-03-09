from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from core.database import get_db
from models.domain import User, Product, Order
from schemas.pydantic_dtos import (UserCreate, UserResponse, ProductCreate, 
                                   ProductResponse, OrderCreate, OrderResponse, CategoryRevenueResponse)

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
    db_product = Product(name=product.name, price=product.price, category=product.category)

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product 

# --- ENDPOINT DE ORDENES ---
@router.post("/orders/", response_model=OrderResponse)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):

    # 1. Buscamos el producto en la base de datos para saber su precio
    product = db.query(Product).filter(Product.id == order.product_id).first()
    # Buscamos tambien el usurio
    user = db.query(User).filter(User.id == order.user_id).first()

    # 2. Validacion de seguridad para asegurarnos de que ese producto si existe
    if not product:
        raise HTTPException(status_code=404, detail="El producto no existe")
    if not user:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    
    # 3. Calculamos el total de la orden
    total_amount = product.price * order.quantity

    # 4. Creamos la transaccion a la base de datos
    db_order = Order(
        user_id =  order.user_id,
        product_id = order.product_id,
        quantity = order.quantity,
        total_amount = total_amount
    )

    # 5. Guardamos
    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    return db_order

# --- ENDPOINT DE INGRESOS POR CATEGORIA ---
@router.get("/analytics/revenue-by-category", response_model=list[CategoryRevenueResponse])
def get_category_revenue(db: Session = Depends(get_db)):
    result = db.query(
        Product.category.label("category"),
        func.sum(Order.total_amount).label("total_revenue")
    )\
    .join(Order, Product.id == Order.product_id)\
    .group_by(Product.category)\
    .all()

    return result