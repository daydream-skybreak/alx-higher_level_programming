#!/usr/bin/python3
"""
module for a square that inherits from class rectangle
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ class for a square """
    def __init__(self, size):
        """ instantiation of square """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """ string representation of the object"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
