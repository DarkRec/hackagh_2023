from fastapi import FastAPI
from app.routers import auth, ocena, przemiot, student, kierunek, wykladowca

app = FastAPI()
