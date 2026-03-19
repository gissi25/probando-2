from sqlalchemy import Column, Integer, String, ForeignKey, Date, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base
import enum


class EstadoLibro(str, enum.Enum):
    DISPONIBLE = "disponible"
    PRESTADO = "prestado"
    RESERVADO = "reservado"
    MANTENIMIENTO = "mantenimiento"


class Libro(Base):
    __tablename__ = "libros"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(200), nullable=False, index=True)
    isbn = Column(String(13), unique=True, nullable=False, index=True)
    autor_id = Column(Integer, ForeignKey("autores.id"), nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)
    año_publicacion = Column(Integer, nullable=False)
    editorial = Column(String(100), nullable=False)
    estado = Column(Enum(EstadoLibro), default=EstadoLibro.DISPONIBLE, nullable=False)
    fecha_creacion = Column(Date, server_default=func.now())
    fecha_actualizacion = Column(Date, onupdate=func.now())

    # Relaciones
    autor = relationship("Autor", back_populates="libros")
    categoria = relationship("Categoria", back_populates="libros")
    prestamos = relationship("Prestamo", back_populates="libro")