from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import date
from enum import Enum


class EstadoLibro(str, Enum):
    DISPONIBLE = "disponible"
    PRESTADO = "prestado"
    RESERVADO = "reservado"
    MANTENIMIENTO = "mantenimiento"


class LibroBase(BaseModel):
    titulo: str = Field(..., min_length=1, max_length=200)
    isbn: str = Field(..., min_length=10, max_length=13)
    autor_id: int
    categoria_id: int
    año_publicacion: int = Field(..., ge=1000, le=date.today().year)
    editorial: str = Field(..., min_length=1, max_length=100)
    estado: EstadoLibro = EstadoLibro.DISPONIBLE

    @validator('isbn')
    def validate_isbn(cls, v):
        # Validación básica de ISBN (puede mejorarse)
        if not v.replace('-', '').replace(' ', '').isdigit():
            raise ValueError('ISBN debe contener solo dígitos, guiones o espacios')
        return v


class LibroCreate(LibroBase):
    pass


class LibroUpdate(BaseModel):
    titulo: Optional[str] = Field(None, min_length=1, max_length=200)
    isbn: Optional[str] = Field(None, min_length=10, max_length=13)
    autor_id: Optional[int] = None
    categoria_id: Optional[int] = None
    año_publicacion: Optional[int] = Field(None, ge=1000, le=date.today().year)
    editorial: Optional[str] = Field(None, min_length=1, max_length=100)
    estado: Optional[EstadoLibro] = None


class LibroInDB(LibroBase):
    id: int
    fecha_creacion: date

    class Config:
        orm_mode = True


class LibroResponse(LibroInDB):
    autor_nombre: Optional[str] = None
    categoria_nombre: Optional[str] = None