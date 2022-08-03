#!/usr/bin/python3
"""
module for a square that inherits from class rectangle
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ class for a square """
    def __init__(self, size):
        """ instantiation of square """
        super().__init__(size, size)
