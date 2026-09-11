import os
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from pydantic import BaseModel

# 1. Configuración de Base de Datos
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:@localhost/mis_tareas_db")

# Creación de 'engine' (soluciona el error en bind=engine)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# 2. Modelo de la Base de Datos (Soluciona el subrayado en 'Tarea')
class Tarea(Base):
    __tablename__ = "tareas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(250), nullable=False)
    descripcion = Column(String(500), nullable=True)


# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)


# 3. Esquema Pydantic para recibir datos en el POST
class TareaCrear(BaseModel):
    titulo: str
    descripcion: str


# 4. Instancia de la aplicación (Soluciona el subrayado en '@app')
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 5. Dependencia para obtener la sesión de la BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 6. Endpoints
@app.get("/tareas")
def obtener_tareas(db: Session = Depends(get_db)):
    return db.query(Tarea).all()


@app.post("/tareas")
def crear_tarea(tarea: TareaCrear, db: Session = Depends(get_db)):
    nueva_tarea = Tarea(titulo=tarea.titulo, descripcion=tarea.descripcion)
    db.add(nueva_tarea)
    db.commit()
    db.refresh(nueva_tarea)
    return nueva_tarea