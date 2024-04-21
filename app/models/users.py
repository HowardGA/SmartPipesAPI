'''
    Everything that has to do with user activity
'''
from pydantic import BaseModel, EmailStr
from pydantic.dataclasses import dataclass


# Base data structure of the user, can use in many other things by inheriting
class UserBase(BaseModel):
    name: str
    phone: str
    email: EmailStr
    role: str
    theme: str
    status: str

class UserCreate(UserBase):
    password: str

@dataclass
class UserLogin:
    email: EmailStr
    password: str