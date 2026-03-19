from sqlalchemy import Column, Integer, String, Date, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class Autor(Base):
    __tablename__ = "autores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False, index=True)
    apellido = Column(String(100), nullable=False, index=True)
    nacionalidad = Column(String(50))
    fecha_nacimiento = Column(Date)
    biografia = Column(Text)
    fecha_creacion = Column(Date, server_default=func.now())

    # Relaciones
    libros = relationship("Libro", back_populates="autor")