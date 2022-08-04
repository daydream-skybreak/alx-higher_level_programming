#!/usr/bin/python3
"""
Base class instantiation module
"""


class Base:
    """base class for all the other classes in this project"""
    __nb_object = 0
    def __init__(self, id=None):
        """ instantiation function """
        if id is None:
            self.__nb_object += 1
            self.id = self.__nb_object
        else:
            self.id = id
