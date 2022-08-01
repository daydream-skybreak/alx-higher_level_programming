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
        raise Exception("area() is not implemented")
