from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base
import enum

class EstadoPrestamo(str, enum.Enum):
    ACTIVO = "activo"
    DEVUELTO = "devuelto"
    VENCIDO = "vencido"
    PERDIDO = "perdido"

class Prestamo(Base):
    __tablename__ = "prestamos"

    id = Column(Integer, primary_key=True, index=True)
    libro_id = Column(Integer, ForeignKey("libros.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    fecha_prestamo = Column(DateTime(timezone=True), server_default=func.now())
    fecha_devolucion_estimada = Column(DateTime(timezone=True))
    fecha_devolucion_real = Column(DateTime(timezone=True))
    estado = Column(Enum(EstadoPrestamo), default=EstadoPrestamo.ACTIVO)
    observaciones = Column(String(500))
    
    # Relaciones
    libro = relationship("Libro")
    usuario = relationship("Usuario")

    def __repr__(self):
        return f"<Prestamo {self.id} - Libro: {self.libro_id}>"