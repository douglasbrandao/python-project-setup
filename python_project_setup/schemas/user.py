from datetime import datetime
from pydantic import BaseModel


class UserBaseSchema(BaseModel):
    name: str
    email: str


class UserCreateSchema(UserBaseSchema):
    password: str


class UserSchema(UserBaseSchema):
    
    class Config:
        orm_mode = True
