from sqlalchemy.orm import Session
from models.domain import User

def create_user_in_db(db: Session, name: str, email: str):
    # Guardamos en la base de datos
    new_user = User(name=name, email=email)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()