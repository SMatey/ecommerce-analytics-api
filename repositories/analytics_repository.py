from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from models.domain import Order, Product

# --- INGRESOS POR CATEGORIA ---
def get_revenue_by_category_from_db(db: Session):
    result = db.query(
        Product.category.label("category"),
        func.sum(Order.total_amount).label("total_revenue")
    )\
    .join(Order, Product.id == Order.product_id)\
    .group_by(Product.category)\
    .all()

    return result

# --- VENTAS POR PRODUCTO ---
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

# --- TENDENCIA DE VENTAS ---
def get_sales_trend_from_db(db: Session):
    # Definimos una Window function para sacar el promedio movil de los ultimos 5 pedidos (orden actual + 4 anteriores)
    moving_average = (
        func.avg(Order.total_amount).over(
            order_by = Order.order_date,
            rows=(-4, 0) # Tomamos las 4 filas precedentes y la fila actual
        )
    ) 

    result = db.query(  
        Order.id.label("order_id"),
        Order.total_amount.label("total_amount"),
        moving_average.label("moving_average")
    )\
    .all()

    return result