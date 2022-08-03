#!/usr/bin/python3
"""
module for exception raising
"""


class BaseGeometry:
    """
    func:
      area: raises an error
    """

    def area(self):
        """ raises an error of area not being implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates `value` to be of a certain criteria """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
