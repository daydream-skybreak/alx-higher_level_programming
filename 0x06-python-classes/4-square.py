#!/usr/bin/python3

""" define a class for a square """


class Square:
    """ represents a square """
    def __init__(self, size=0):
        """ initializing the instance variable

        Args:
            size (int): length of the square side
        """
        self.size = size
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2
