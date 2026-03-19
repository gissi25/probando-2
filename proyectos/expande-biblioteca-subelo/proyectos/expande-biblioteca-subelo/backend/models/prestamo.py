from sqlalchemy import Column, Integer, ForeignKey, Date, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base
import enum


class EstadoPrestamo(str, enum.Enum):
    ACTIVO = "activo"
    DEVUELTO = "devuelto"
    VENCIDO = "vencido"
    CANCELADO = "cancelado"


class Prestamo(Base):
    __tablename__ = "prestamos"

    id = Column(Integer, primary_key=True, index=True)
    libro_id = Column(Integer, ForeignKey("libros.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    fecha_prestamo = Column(Date, server_default=func.now(), nullable=False)
    fecha_devolucion_prevista = Column(Date, nullable=False)
    fecha_devolucion_real = Column(Date)
    estado = Column(Enum(EstadoPrestamo), default=EstadoPrestamo.ACTIVO, nullable=False)
    observaciones = Column(Text)

    # Relaciones
    libro = relationship("Libro", back_populates="prestamos")
    usuario = relationship("Usuario", back_populates="prestamos")