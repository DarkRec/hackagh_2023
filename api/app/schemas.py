from pydantic import BaseModel, Field

class Car(BaseModel):
    id: int = Field(...)
    ownerID: int = Field(...)
    otherUsers: str = Field(...)
    country: str = Field(...)
    location: str = Field(...)
    info: str = Field(...)

class Info():
    RegistrationNumbers: str = Field(...)
    Brand: str = Field(...)
    Model: str = Field(...)
    

class User(BaseModel):
    id: int = Field(...)
    name: str = Field(...)
    lastname: str = Field(...)
    settings: str = Field(...)

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