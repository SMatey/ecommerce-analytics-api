from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from models.domain import Order, Product

def get_revenue_by_category_from_db(db: Session):
    result = db.query(
        Product.category.label("category"),
        func.sum(Order.total_amount).label("total_revenue")
    )\
    .join(Order, Product.id == Order.product_id)\
    .group_by(Product.category)\
    .all()

    return result

def get_top_products_from_db(db: Session):
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