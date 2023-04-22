from fastapi import FastAPI
from app.config import settings
from pymongo import MongoClient



app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(settings.CONNECTION_STRING)
    app.database = app.mongodb_client[settings.DB_NAME]

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()