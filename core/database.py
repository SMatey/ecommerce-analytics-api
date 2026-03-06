from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from core.config import DATABASE_URL

# Creamos el conector a la base de datos
engine = create_engine(str(DATABASE_URL), echo=True)

# Creamos la fabrica de sessiones (sessionmaker)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Creamos la base (molde para crear tablas despues)
Base = declarative_base()

def get_db ():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()