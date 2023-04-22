from fastapi import Depends, HTTPException, APIRouter, status
from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from app.db.models import *
from app.config import settings
from app.schemas import Car

router = APIRouter()

@router.get(f"/api/{settings.VERSION}")
def get_cars():
    return {"response": "Get cars"}


@router.get("/{car_id}")
async def get_single_user(user_id: str):
    return {"response": f"Get user: {user_id}"}

@router.post("/", response_description="Create a new car", status_code=status.HTTP_201_CREATED, response_model=Car)
def create_car(request: Request, car: Car = Body(...)):
    car = jsonable_encoder(car)
    new_car = request.app.database["cars"].insert_one(car)
    created_car = request.app.database["cars"].find_one(
        {"_id": new_car.inserted_id}
    )

    return created_car