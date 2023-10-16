#!usr/bin/python3
"""
    Class City that inherits from BaseModel,
    and contains all data about city class.
"""
from .base_model import BaseModel


class City(BaseModel):
    """
    Represents all the attributes.
    """
    state_id = ""
    name = ""
