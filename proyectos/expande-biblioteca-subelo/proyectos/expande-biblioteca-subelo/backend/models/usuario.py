from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    telefono = Column(String(20))
    direccion = Column(String(200))
    fecha_registro = Column(Date, server_default=func.now())
    activo = Column(Boolean, default=True, nullable=False)

    # Relaciones
    prestamos = relationship("Prestamo", back_populates="usuario")