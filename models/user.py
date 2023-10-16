#!usr/bin/python3
"""
    Class User that inherits from BaseModel,
    and contains all data about user class
"""
from .base_model import BaseModel


class User(BaseModel):
    """
    Represents all the attributes.

    Attributes:
        email = user's email
        password = user's email
        first_name = user's first name
        last_name = user's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
