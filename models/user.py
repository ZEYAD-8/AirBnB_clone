#!usr/bin/python3
"""
    Class User that inherits from BaseModel,
    and contains all data about user class
"""
from .base_model import BaseModel


class User(BaseModel):
    """
    Represents all the attributes.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
