from fastapi import Depends, HTTPException, APIRouter, status
from app.db.models import *

router = APIRouter()

@router.get("/api/v1/users/")
async def users_main():
    return {"response": "It works!"}


@router.get("/api/v1/users/{user_id}")
async def get_single_user(user_id: str):
    return {"response": f"Get user: {user_id}"}


@router.post("/api/v1/users/")
async def create_user(user):
    return {"response": "It works: users post"}


@router.patch("/api/v1/users/{user_id}")
async def edit_user(user_id: str):
    return {"response": f"Edit user: {user_id}"}


@router.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: str, user):
    return {"response": f"Delete user: {user_id}"}


