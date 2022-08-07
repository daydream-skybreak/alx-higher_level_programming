#!/usr/bin/python3
"""
Base class instantiation module
"""


import json


class Base:
    """base class for all the other classes in this project"""
    __nb_object = 0

    def __init__(self, id=None):
        """ instantiation function
        Args:
            id: id of instances
        """
        if id is None:
            Base.__nb_object += 1
            self.id = Base.__nb_object
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON Serialization of a list of dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """that writes the JSON string representation of list_objs to a file
        Args:
            list_objs: list of objects of a certain class
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dict = [ob.to_dictionary() for ob in list_objs]
                file.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of deserialized the JSON string
        Args:
            json_string: as the name suggests
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dumy = cls(1, 1)
        else:
            dumy = cls(1)
        dumy.update(**dictionary)
        return dumy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances from a .json file
        returns an empty list if the file doesn't exist
        """
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, "r") as file:
                list_dict = Base.from_json_string(file.read())
                return [cls.create(**d) for d in list_dict]
        except IOError:
            return []
