#!/usr/bin/python3
"""
module for class representation of a rectangle
"""
from models.base import Base

class Rectangle(Base):
    """class that is a representation of a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes a new rectangle

        Args:
            height: height of the rectangle
            width: width of the rectangle
            x: the x-coordinate of the new rectangle (default=0)
            y: the y-coordinate of the new rectangle (default=0)
            id (int): id of the new triangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ set and get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width


    @property
    def height(self):
        """ set and get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height
        
    @property
    def x(self):
        """get and set x coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x
    
    @property
    def y(self):
        """get and set y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
