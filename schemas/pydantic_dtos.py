from pydantic import BaseModel, ConfigDict
from datetime import datetime

# --- ESQUEMAS PARA USUARIOS ---

# Lo que el cliente envia
class UserCreate(BaseModel):
    email: str
    name: str

# Lo que la base de datos devuelve
class UserResponse(BaseModel):
    id: int
    email: str
    name: str
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)

# --- ESQUEMAS PARA PRODUCTOS ---

class ProductCreate(BaseModel):
    name: str
    price: float
    category: str

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    category: str

    model_config = ConfigDict(from_attributes=True) 