from sqlalchemy.orm import Session
from fastapi import HTTPException
from repositories import analytics_repository
from schemas.pydantic_dtos import CategoryRevenueResponse, TopProductResponse

def get_category_revenue(db: Session):
    return analytics_repository.get_revenue_by_category_from_db(db)

def get_top_products(db: Session):
    return analytics_repository.get_top_products_from_db(db)