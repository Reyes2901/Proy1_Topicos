from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models, schemas

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/detalle")
def crear_detalle(detalle: schemas.DetalleCreate, db: Session = Depends(get_db)):
    nuevo = models.DetalleVenta(**detalle.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@router.get("/detalle")
def listar_detalles(db: Session = Depends(get_db)):
    return db.query(models.DetalleVenta).all()