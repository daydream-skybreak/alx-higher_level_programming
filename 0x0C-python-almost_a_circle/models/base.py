#!/usr/bin/python3
"""
Base class instantiation module
"""


import json


class Base:
    """base class for all the other classes in this project"""
    __nb_object = 0
    def __init__(self, id=None):
        """ instantiation function """
        if id is None:
            Base.__nb_object += 1
            self.id = Base.__nb_object
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json representation of a list of dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
