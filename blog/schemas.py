""" pass """
from typing import List

from pydantic import BaseModel


class BlogBase(BaseModel):
    """ pass """
    title: str
    body: str


class Blog(BlogBase):
    """pass"""

    class Config:
        """ pass """
        orm_mode = True


class User(BaseModel):
    """ pass """
    name: str
    email: str
    password: str


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
