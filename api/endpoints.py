from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from core.database import get_db
from schemas.pydantic_dtos import (UserCreate, UserResponse, ProductCreate, 
                                   ProductResponse, OrderCreate, OrderResponse, 
                                   CategoryRevenueResponse, TopProductResponse)
from services import (user_service, product_service, order_service)

# creamos el enrutador
router = APIRouter()

# --- ENDPOINT DE USUARIOS ---
@router.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Llamamos el servicio para crear un nuevo usuario
    return user_service.create_new_user(db, user)

# --- ENDPOINT DE PRODUCTOS ---
@router.post("/products/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    # Llamamos el servicio para crear un nuevo producto
    return product_service.create_new_product(db, product) 

# --- ENDPOINT DE ORDENES ---
@router.post("/orders/", response_model=OrderResponse)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    # Llamamos el servicio para crear una nueva orden
    return order_service.create_new_order(db, order)

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

# --- ENDPOINT DE TOP PRODUCTOS ---
@router.get("/analytics/top-products", response_model=list[TopProductResponse])
def get_top_products(db: Session = Depends(get_db)):
    result = db.query(
        Product.name.label("product_name"),
        func.sum(Order.quantity).label("total_quantity_sold")
    )\
    .join(Order, Product.id == Order.product_id)\
    .group_by(Product.name)\
    .order_by(desc("total_quantity_sold"))\
    .limit(5)\
    .all()

    return result