#!usr/bin/python3
"""
    Class Review that inherits from BaseModel,
    and contains all data about review class.
"""
from .base_model import BaseModel


class Review(BaseModel):
    """
    Represents all the attributes.

    Attrributes:
        place_id = place.id()
        user_id = user.id()
        text = text review
    """
    place_id = ""
    user_id = ""
    text = ""
