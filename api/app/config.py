from pydantic import BaseSettings

class Settings(BaseSettings):
    CONNECTION_STRING: str
    
    class Config:
        env_file = ".env"

settings = Settings()