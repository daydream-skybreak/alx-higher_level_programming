#!/usr/bin/python3
"""
module for exception raising
"""


class BaseGeometry:
    """
    func:
      area: raises an error
    """
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} has to be an integer".format(self.name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
