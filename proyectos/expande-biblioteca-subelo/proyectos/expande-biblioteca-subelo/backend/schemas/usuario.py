from pydantic import BaseModel, Field, EmailStr, validator
from typing import Optional
from datetime import date
import re


class UsuarioBase(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    telefono: Optional[str] = Field(None, max_length=20)
    direccion: Optional[str] = Field(None, max_length=200)

    @validator('telefono')
    def validate_telefono(cls, v):
        if v and not re.match(r'^[\d\s\-\+\(\)]+$', v):
            raise ValueError('Teléfono debe contener solo dígitos, espacios, guiones, paréntesis o signo +')
        return v


class UsuarioCreate(UsuarioBase):
    pass


class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = Field(None, min_length=1, max_length=100)
    email: Optional[EmailStr] = None
    telefono: Optional[str] = Field(None, max_length=20)
    direccion: Optional[str] = Field(None, max_length=200)
    activo: Optional[bool] = None


class UsuarioInDB(UsuarioBase):
    id: int
    fecha_registro: date
    activo: bool

    class Config:
        orm_mode = True


class UsuarioResponse(UsuarioInDB):
    prestamos_activos: int = 0