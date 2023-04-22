from fastapi import Depends, HTTPException, APIRouter, status
from app.db.models import *
from app.config import settings

router = APIRouter()

@router.get(f"/api/{settings.VERSION}")
def get_cars():
    return {"response": "Get cars"}