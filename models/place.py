#!usr/bin/python3
"""
    Class Place that inherits from BaseModel,
    and contains all data about place class.
"""
from .base_model import BaseModel


class Place(BaseModel):
    """
    Represents all the attributes.

    Attributes:
        city_id = city.id()
        user_id = user.id()
        name = place_name
        description = information about the place
        number_rooms = number of rooms
        max_guest = maximum numbers of guests
        price_by_night = the cost of the place for night
        latitude = exact coordinates for the place
        longitude = exact coordinates for the place
        amenity_ids = list of amenity.id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
