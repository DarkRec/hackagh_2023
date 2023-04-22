from fastapi import Depends, HTTPException, APIRouter, status
from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from app.db.models import *
from app.config import settings
from app.schemas import Car, Location

router = APIRouter()

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


@router.patch("/location/")
def change_location(request: Request, location: Location = Body(...)):
    location = jsonable_encoder(location)
    # location = {k:v for k,v in location.dict().items() if v is not None}
    # print(location.id)
    # my_query = {"_id": location['id']}
    to_edit = request.app.database["cars"].update_one(
        {"_id": location['id']}, {"$set": {"location": location['location']}}
        # {"_id", location]id}, {"$set": {"location": location.location}}
    )

    if to_edit.modified_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Car with ID {location['id']} not found")
    else:
        return {"response": f"position changed: {location['location']}"}