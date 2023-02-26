""" pass """
from typing import List, Optional

from pydantic import BaseModel


class BlogBase(BaseModel):
    """ pass """
    title: str
    body: str


class Blog(BlogBase):
    """pass"""
    user_id: int

    class Config:
        """ pass """
        orm_mode = True


class UserBase(BaseModel):
    """ pass """
    name: str
    email: str
    password: str

    class Config:
        """ pass """
        orm_mode = True


class User(UserBase):
    """ pass """
    name: str
    email: str

    class Config:
        """ pass """
        orm_mode = True


class ShowUser(User):
    """ pass """
    name: str
    email: str
    blogs: List[Blog] = []

    class Config:
        """ pass """
        orm_mode = True


class ShowBlog(Blog):
    """ pass """
    title: str
    body: str
    creator: ShowUser

    class Config:
        """ pass """
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
