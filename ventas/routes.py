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


@router.post("/ventas")
def crear_venta(venta: schemas.VentaCreate, db: Session = Depends(get_db)):
    nueva = models.Venta(**venta.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva


@router.get("/ventas")
def listar_ventas(db: Session = Depends(get_db)):
    return db.query(models.Venta).all()