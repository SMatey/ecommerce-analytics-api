from sqlalchemy.orm import Session
from models.domain import Product

def create_product_in_db(db: Session, name: str, price: float, category: str):
    # Guardamos en la base de datos
    new_product = Product(name=name, price=price, category=category)

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product

def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()