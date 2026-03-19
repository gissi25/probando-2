from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import date
from enum import Enum


class EstadoPrestamo(str, Enum):
    ACTIVO = "activo"
    DEVUELTO = "devuelto"
    VENCIDO = "vencido"
    CANCELADO = "cancelado"


class PrestamoBase(BaseModel):
    libro_id: int
    usuario_id: int
    fecha_devolucion_prevista: date
    observaciones: Optional[str] = None

    @validator('fecha_devolucion_prevista')
    def validate_fecha_devolucion(cls, v, values):
        if v <= date.today():
            raise ValueError('La fecha de devolución prevista debe ser futura')
        return v


class PrestamoCreate(PrestamoBase):
    pass


class PrestamoUpdate(BaseModel):
    fecha_devolucion_real: Optional[date] = None
    estado: Optional[EstadoPrestamo] = None
    observaciones: Optional[str] = None


class PrestamoInDB(PrestamoBase):
    id: int
    fecha_prestamo: date
    fecha_devolucion_real: Optional[date] = None
    estado: EstadoPrestamo

    class Config:
        orm_mode = True


class PrestamoResponse(PrestamoInDB):
    libro_titulo: Optional[str] = None
    usuario_nombre: Optional[str] = None
    dias_restantes: Optional[int] = None