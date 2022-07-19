#!/usr/bin/python3

""" define a class for a square """


class Square:
    """ represents a square """
    def __init__(self, size):
        """ initializing the instance variable

        Args:
            size (int): length of the square side
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
