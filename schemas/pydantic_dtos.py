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

# --- ESQUEMAS PARA ORDENES ---
class OrderCreate(BaseModel):
    user_id: int
    product_id: int
    quantity: int

class OrderResponse(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity:  int
    total_amount: float
    order_date:  datetime

    model_config = ConfigDict(from_attributes=True)

# --- ESQUEMA PARA INGRESOS POR CATEGORIA ---
class CategoryRevenueResponse(BaseModel):
    category: str
    total_revenue: float

    model_config = ConfigDict(from_attributes=True)

# --- ESQUEMA PARA TOP PRODUCTOS ---
class TopProductResponse(BaseModel):
    product_name: str
    total_quantity_sold: int

    model_config = ConfigDict(from_attributes=True)

# --- ESQUEMA PARA SALES TREND ---
class SalesTrendResponse(BaseModel):
    order_id: int
    total_amount: float
    moving_average: float

    model_config = ConfigDict(from_attributes=True)