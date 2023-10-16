#!/usr/bin/python3
"""
Defines the FileStorage class.
"""
import json
import datetime
from ..base_model import BaseModel
from ..user import User
from ..state import State
from ..city import City
from ..amenity import Amenity
from ..place import Place
from ..review import Review


class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        return super().default(obj)


class FileStorage():
    """
    Represent an abstracted storage engine.

    Attr:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = 'file.json'
    __objects = {}
    classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
               'Amenity': Amenity, 'City': City, 'Review': Review,
               'Place': Place}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    @classmethod
    def new(cls, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        data_to_save = {
            key: value.to_dict()
            if not isinstance(value, dict) else value
            for key, value in FileStorage.__objects.items()
        }
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(data_to_save, file, cls=DateTimeEncoder)

    def reload(self):
        """
        Deserializes the JSON file to __objects, if it exists.
        """
        if FileStorage.__file_path:
            try:
                with open(FileStorage.__file_path, 'r') as file:
                    FileStorage.__objects = json.load(file)
            except FileNotFoundError:
                return

            for key, value in FileStorage.__objects.items():
                if isinstance(value, dict):
                    for attribute, val in value.items():
                        if attribute == "__class__":
                            className = val
                            # del attribute["__class__"]
                            classF = FileStorage.classes[className]
                            FileStorage.new(classF(**value))
                else:
                    FileStorage.new(value)
