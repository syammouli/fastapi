from pydantic import BaseModel
from typing import List

class Blot(BaseModel):
    name:str
    age:int

from pydantic import BaseModel


class showonlytittle(BaseModel):
    title: str

    class Config:
        orm_mode = True


class user(BaseModel):
    name:str
    email:str
    password:str
    blogs: List[showonlytittle] = []
    class Config:
        orm_mode = True

class Post(BaseModel):
    title: str
    content: str
    creator : user
    class Config:
        orm_mode = True

class ShowUserBasic(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True


# ---------- POST ----------
class ShowPost(BaseModel):
    id: int
    title: str
    content: str

    creator: ShowUserBasic   # 👈 this matches your model field name

    class Config:
        orm_mode = True


class Login(BaseModel):
    email: str
    password: str

class TokenData(BaseModel):
    username: str 
