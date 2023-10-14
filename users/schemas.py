from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    username: str
    email: str
    password: str
    wallet_id: str
    name: str
    last_name: str
    sex_type: str
    dni: str
    birth_date: datetime


class UserUpdate(BaseModel):
    username: str
    email: str
    wallet_id: str
    name: str
    last_name: str
    sex_type: str
    dni: str
    birth_date: datetime


class UserDisplay(BaseModel):
    id: int
    username: str
    email: str
    wallet_id: str
    name: str
    last_name: str
    sex_type: str
    dni: str
    birth_date: datetime

    class Config:
        from_attributes = True
