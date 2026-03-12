from pydantic import BaseModel, EmailStr, Field


class ClienteCreate(BaseModel):

    nombre: str = Field(min_length=3, max_length=100)
    telefono: str = Field(min_length=7, max_length=15)
    email: EmailStr


class ProductoCreate(BaseModel):

    nombre: str = Field(min_length=2, max_length=100)
    precio: float = Field(gt=0)
    stock: int = Field(ge=0)


class VentaCreate(BaseModel):

    cliente_id: int
    total: float = Field(gt=0)


class DetalleCreate(BaseModel):

    venta_id: int
    producto_id: int
    cantidad: int = Field(gt=0)
    subtotal: float = Field(gt=0)