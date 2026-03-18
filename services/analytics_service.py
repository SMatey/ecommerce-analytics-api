from sqlalchemy.orm import Session
from fastapi import HTTPException
from repositories import analytics_repository

# --- INGRESOS POR CATEGORIA ---
def get_category_revenue(db: Session):
    return analytics_repository.get_revenue_by_category_from_db(db)

# --- VENTAS POR PRODUCTO ---
def get_top_products(db: Session):
    return analytics_repository.get_top_products_from_db(db)

# --- TENDENCIA DE VENTAS ---
def get_sales_trend(db: Session):
   return analytics_repository.get_sales_trend_from_db(db)

# --- RETENCION DE USUARIOS ---
def get_cohort_retention_users(db: Session):
    return analytics_repository.get_cohort_retention_users_from_db(db)