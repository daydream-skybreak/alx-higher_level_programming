#!/usr/bin/python3
"""
module for class representation of a rectangle
"""
from models.base import Base
# from base import Base

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
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ set and get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """get and set x coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """get and set y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """computes and returns the area of the rectangle"""
        return self.height * self.width

    def display(self):
        """displays the rectangle using `#` representation"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for i in range(self.y)]

        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def update(self, *args):
        """updates the rectangle based on the arguments passed to it"""
        if args and len(args) != 0:
            for arg in args:
                i = 0
                if i == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = 1
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1

    def __str__(self):
        """Returns a string representeaioln of the Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                     self.width, self.height)
