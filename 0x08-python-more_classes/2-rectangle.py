#!/usr/bin/python3
""" Defines a class for creating rectangles """


class Rectangle:
    """ a rectangle class with private width and height"""
    def __init__(self, width=0, height=0):
        """ an instance method to be called when new object is created """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle """
        self.__width * self.__height

    def perimeter(self):
        """ returns the perimeter of the rectangle """
        2 * (self.__width + self.__height)












































