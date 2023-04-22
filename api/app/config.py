from pydantic import BaseSettings

class Settings(BaseSettings):
    CONNECTION_STRING: str
    DB_NAME: str
    VERSION: str
    
    class Config:
        env_file = ".env"

settings = Settings()