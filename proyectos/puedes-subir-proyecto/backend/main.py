from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routes import libros, prestamos, usuarios

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sistema de Gestión de Biblioteca API",
    description="API para gestionar inventario de biblioteca",
    version="1.0.0"
)

# Configurar CORS para permitir conexiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas
app.include_router(libros.router, prefix="/api", tags=["Libros"])
app.include_router(prestamos.router, prefix="/api", tags=["Préstamos"])
app.include_router(usuarios.router, prefix="/api", tags=["Usuarios"])

@app.get("/")
def read_root():
    return {"message": "Bienvenido al Sistema de Gestión de Biblioteca API"}

@app.get("/api/health")
def health_check():
    return {"status": "healthy", "service": "biblioteca-api"}