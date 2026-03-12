from fastapi import FastAPI
import models
from database import engine

from clientes.routes import router as clientes_router
from productos.routes import router as productos_router
from ventas.routes import router as ventas_router
from detalle_ventas.routes import router as detalle_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="ERP Ventas con PostgreSQL")

app.include_router(clientes_router)
app.include_router(productos_router)
app.include_router(ventas_router)
app.include_router(detalle_router)


@app.get("/")
def inicio():
    return {"mensaje": "ERP funcionando con PostgreSQL"}