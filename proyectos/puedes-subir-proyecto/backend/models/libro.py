from sqlalchemy import Column, Integer, String, Text, Enum, DateTime
from sqlalchemy.sql import func
from database import Base
import enum

class EstadoLibro(str, enum.Enum):
    DISPONIBLE = "disponible"
    PRESTADO = "prestado"
    RESERVADO = "reservado"
    MANTENIMIENTO = "mantenimiento"
    PERDIDO = "perdido"

class Libro(Base):
    __tablename__ = "libros"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(200), nullable=False, index=True)
    autor = Column(String(150), nullable=False)
    isbn = Column(String(20), unique=True, nullable=False, index=True)
    editorial = Column(String(100))
    año_publicacion = Column(Integer)
    categoria = Column(String(100))
    estado = Column(Enum(EstadoLibro), default=EstadoLibro.DISPONIBLE)
    ubicacion = Column(String(50))
    descripcion = Column(Text)
    cantidad_total = Column(Integer, default=1)
    cantidad_disponible = Column(Integer, default=1)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<Libro {self.titulo} - {self.autor}>"