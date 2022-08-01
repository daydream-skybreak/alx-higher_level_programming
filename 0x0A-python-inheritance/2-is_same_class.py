#!/usr/bin/python3
""" module for function to check instances are of the specified class"""


def is_same_class(obj, a_class):
    """ function to determine if obj is instance of a_class """
    return isinstance(obj, a_class)
