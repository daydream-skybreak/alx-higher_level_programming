#!/usr/bin/python3

""" define a class for a square """


class Square:
    """ represents a square """
    def __init__(self, size):
        """ initializing the instance variable

        Args:
            size (int): length of the square side
        """
        self.__size = size
