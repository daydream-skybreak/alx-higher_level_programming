#!/usr/bin/python3
""" module for class rectangle """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class for rectangle metrics instantiation"""
    def __init__(self, width, height):
        """ class instantiation method """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns the string representation of the class"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
