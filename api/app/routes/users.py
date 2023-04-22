from fastapi import Depends, HTTPException, APIRouter, status
from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from app.db.models import *
from uuid import uuid4
from app.schemas import User, newUser

router = APIRouter()

@router.get("/")

async def users_main():
    return {"response": "It works!"}


@router.get("/{user_id}")
async def get_single_user(user_id: str):
    return {"response": f"Get user: {user_id}"}


@router.post("/", response_description="Create a new user", status_code=status.HTTP_201_CREATED)#, response_model=User
def create_user(request: Request, user: User = Body(...)):
    user = jsonable_encoder(user)
    #user.id = randon_uid = str(uuid4())
    new_user = request.app.database["users"].insert_one(user)
    #created_user = request.app.database["users"].find_one(
    #    {"_id": new_user.inserted_id}
    #)

    #return created_user

@router.patch("/{user_id}")
async def edit_user(user_id: str):
    return {"response": f"Edit user: {user_id}"}


@router.delete("/{user_id}")
async def delete_user(user_id: str, user):
    return {"response": f"Delete user: {user_id}"}


