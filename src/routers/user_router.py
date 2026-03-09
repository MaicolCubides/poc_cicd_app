from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)  # Utilidades de FastAPI, Depends es el sistema de inyeccion de dependencias de FastAPI
from sqlalchemy.orm import Session  # Representa la conexión activa con la base de datos
from src.core.database import SessionLocal  # Armar una nueva conexion
from src.schemas.user import UserCreate, UserResponse
from src.services import user_service

router = APIRouter(prefix="/users", tags=["users"])  # Agrupamos los enpoings


# Creamos una conexion de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=UserResponse)
def create(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)


@router.get("/", response_model=list[UserResponse])
def read_all(db: Session = Depends(get_db)):
    return user_service.get_users(db)


@router.get("/{user_id}", response_model=UserResponse)
def read_one(user_id: int, db: Session = Depends(get_db)):
    user = user_service.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.delete("/{user_id}")
def delete(user_id: int, db: Session = Depends(get_db)):
    user = user_service.delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}
