from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime
from enum import Enum

class EstadoPrestamo(str, Enum):
    ACTIVO = "activo"
    DEVUELTO = "devuelto"
    VENCIDO = "vencido"
    PERDIDO = "perdido"

class PrestamoBase(BaseModel):
    libro_id: int = Field(..., gt=0)
    usuario_id: int = Field(..., gt=0)
    fecha_devolucion_estimada: Optional[datetime] = None
    observaciones: Optional[str] = Field(None, max_length=500)

class PrestamoCreate(PrestamoBase):
    pass

class PrestamoUpdate(BaseModel):
    fecha_devolucion_real: Optional[datetime] = None
    estado: Optional[EstadoPrestamo] = None
    observaciones: Optional[str] = Field(None, max_length=500)

class PrestamoResponse(PrestamoBase):
    id: int
    fecha_prestamo: datetime
    fecha_devolucion_real: Optional[datetime]
    estado: EstadoPrestamo
    created_at: datetime
    updated_at: Optional[datetime]
    
    # Información relacionada
    libro_titulo: Optional[str] = None
    libro_autor: Optional[str] = None
    usuario_nombre: Optional[str] = None
    usuario_apellido: Optional[str] = None

    class Config:
        from_attributes = True