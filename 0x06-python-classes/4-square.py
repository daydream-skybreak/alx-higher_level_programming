#!/usr/bin/python3


class Square:
    '''Class Square
    '''
    pass

    def __init__(self, size=0):
        '''init method of class Square
        Args:
            size (int): integer argument for the class 'Square'
        '''
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
