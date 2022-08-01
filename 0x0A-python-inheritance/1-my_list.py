#!/usr/bin/python3
""" module for MyList class """


class MyList(list):
    """class that prints out a sorted list
       It inherits from the built-in class 'list'
    """
    def __init__(self):
        return super().__init__()

    def print_sorted(self):
        """ function to print sorted list"""
        print(sorted(self))
