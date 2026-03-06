from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from src.routers import user_router
from src.routers import health_router
from src.core.database import Base, engine

app = FastAPI(title="CRUD FastAPI Users")

Base.metadata.create_all(bind=engine)

app.include_router(user_router.router)
app.include_router(health_router.router)

Instrumentator().instrument(app).expose(app)

