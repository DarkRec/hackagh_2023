from pydantic import BaseModel, Field
import uuid

class Car(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    ownerID: str = Field(...)
    adminsList: str = Field(...)
    usersList: str = Field(...)
    country: str = Field(...)
    location: str = Field(...)
    info: str = Field(...)

class Info():
    RegistrationNumbers: str = Field(...)
    Brand: str = Field(...)
    Model: str = Field(...)
    
class Settings(BaseModel):
    leftMirrorX: int = Field(...)
    leftMirrorY: int = Field(...)
    rightMirrorX: int = Field(...)
    rightMirrorY: int = Field(...)
    rearMirrorX: int = Field(...)
    rearMirrorY: int = Field(...)
    driverSeatX: int = Field(...)
    driverSeatY: int = Field(...)
    driverSeatAngle: int = Field(...)
    passengerSeatX: int = Field(...)
    passengerSeatY: int = Field(...)
    passengerSeatAngle: int = Field(...)
    steeringWheelX: int = Field(...)
    steeringWheelY: int = Field(...)

class User(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id", index=True, nullable=False)
    name: str = Field(...)
    lastname: str = Field(...)
    settings: Settings = Field(...)

    class Config:
        allow_population_by_field_name = True


class newUser(BaseModel):
    name: str = Field(...)
    lastname: str = Field(...)