#!usr/bin/python3
"""
    Class City that inherits from BaseModel,
    and contains all data about city class.
"""
from .base_model import BaseModel


class City(BaseModel):
    """
    Represents all the attributes.

    Attributes:
        state_id = state.id()
        name = city_name
    """
    state_id = ""
    name = ""
