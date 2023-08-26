
from pydantic import BaseModel
from typing import List

class Blog(BaseModel):
    title: str
    body: str

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser
    # class Config():
    #     orm_mode = True

class User(BaseModel):
    name: str
    email: str
    password: str

