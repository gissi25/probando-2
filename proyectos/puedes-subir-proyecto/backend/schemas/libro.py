from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime
from enum import Enum

class EstadoLibro(str, Enum):
    DISPONIBLE = "disponible"
    PRESTADO = "prestado"
    RESERVADO = "reservado"
    MANTENIMIENTO = "mantenimiento"
    PERDIDO = "perdido"

class LibroBase(BaseModel):
    titulo: str = Field(..., min_length=1, max_length=200)
    autor: str = Field(..., min_length=1, max_length=150)
    isbn: str = Field(..., min_length=10, max_length=20)
    editorial: Optional[str] = Field(None, max_length=100)
    año_publicacion: Optional[int] = Field(None, ge=1000, le=datetime.now().year)
    categoria: Optional[str] = Field(None, max_length=100)
    estado: EstadoLibro = EstadoLibro.DISPONIBLE
    ubicacion: Optional[str] = Field(None, max_length=50)
    descripcion: Optional[str] = None
    cantidad_total: int = Field(1, ge=1)
    cantidad_disponible: int = Field(1, ge=0)

    @validator('cantidad_disponible')
    def validate_cantidad_disponible(cls, v, values):
        if 'cantidad_total' in values and v > values['cantidad_total']:
            raise ValueError('cantidad_disponible no puede ser mayor que cantidad_total')
        return v

class LibroCreate(LibroBase):
    pass

class LibroUpdate(BaseModel):
    titulo: Optional[str] = Field(None, min_length=1, max_length=200)
    autor: Optional[str] = Field(None, min_length=1, max_length=150)
    editorial: Optional[str] = Field(None, max_length=100)
    año_publicacion: Optional[int] = Field(None, ge=1000, le=datetime.now().year)
    categoria: Optional[str] = Field(None, max_length=100)
    estado: Optional[EstadoLibro] = None
    ubicacion: Optional[str] = Field(None, max_length=50)
    descripcion: Optional[str] = None
    cantidad_total: Optional[int] = Field(None, ge=1)
    cantidad_disponible: Optional[int] = Field(None, ge=0)

class LibroResponse(LibroBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True