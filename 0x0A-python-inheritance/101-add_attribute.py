#!/usr/bin/python3
"""
module to add an attribute a class
"""


def add_attribute(obj, attr, value):
    """
    a function that adds an attribute to an object
    Args:
        obj: object to which the attribute is to be added
        attr: attribute to be added to the object
        value: value of the attribute
    Raises:
        TypeError
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
