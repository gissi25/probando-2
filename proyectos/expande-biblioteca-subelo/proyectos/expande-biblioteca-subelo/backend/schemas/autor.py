from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import date


class AutorBase(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=100)
    apellido: str = Field(..., min_length=1, max_length=100)
    nacionalidad: Optional[str] = Field(None, max_length=50)
    fecha_nacimiento: Optional[date] = None
    biografia: Optional[str] = None


class AutorCreate(AutorBase):
    pass


class AutorUpdate(BaseModel):
    nombre: Optional[str] = Field(None, min_length=1, max_length=100)
    apellido: Optional[str] = Field(None, min_length=1, max_length=100)
    nacionalidad: Optional[str] = Field(None, max_length=50)
    fecha_nacimiento: Optional[date] = None
    biografia: Optional[str] = None


class AutorInDB(AutorBase):
    id: int
    fecha_creacion: date

    class Config:
        orm_mode = True


class AutorResponse(AutorInDB):
    total_libros: int = 0