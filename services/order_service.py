from sqlalchemy.orm import Session
from fastapi import HTTPException
from repositories import order_repository, user_repository, product_repository
from schemas.pydantic_dtos import OrderCreate

def create_new_order(db: Session, order_data: OrderCreate):
    # Buscamos al usuario
    user = user_repository.get_user_by_id(db, order_data.user_id)
    # Buscamos el producto
    product = product_repository.get_product_by_id(db, order_data.product_id)

    # Realizamos validaciones de que ambos usuario y producto existan
    if not user:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    if not product:
        raise HTTPException(status_code=404, detail="El producto no existe")
    
    # Calculamos el total de la orden
    total_amount = order_data.quantity * product.price

    # Llamamos el repositorio para guarddar en la DB
    return order_repository.create_order_on_db(
        user_id = order_data.user_id,
        product_id = order_data.product_id,
        quantity = order_data.quantity,
        total_amount = total_amount
    )