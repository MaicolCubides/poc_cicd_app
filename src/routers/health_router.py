from fastapi import APIRouter
from src.core.config import settings

router = APIRouter()

@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "env": settings.ENV
    }
