from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class CategoriaBase(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=100)
    descripcion: Optional[str] = None


class CategoriaCreate(CategoriaBase):
    pass


class CategoriaUpdate(BaseModel):
    nombre: Optional[str] = Field(None, min_length=1, max_length=100)
    descripcion: Optional[str] = None


class CategoriaInDB(CategoriaBase):
    id: int
    fecha_creacion: date

    class Config:
        orm_mode = True


class CategoriaResponse(CategoriaInDB):
    total_libros: int = 0