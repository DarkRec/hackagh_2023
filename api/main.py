from fastapi import FastAPI
from app.config import settings
from pymongo import MongoClient
from app.routes import users, cars

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(settings.CONNECTION_STRING)
    app.database = app.mongodb_client[settings.DB_NAME]

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(users.router, tags=['Users'], prefix='/api/v1/users')
app.include_router(cars.router, tags=['Cars'], prefix='/api/v1/cars')