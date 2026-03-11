from sqlalchemy.orm import Session
from models.domain import Order

def create_order_on_db(db: Session, user_id: int, product_id: int, quantity: int, total_amount: float):
    # Guardamos en la base de datos
    new_order = Order(user_id=user_id, product_id=product_id, quantity=quantity, total_amount=total_amount)

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return new_order

