#!/usr/bin/python3
"""functions to print {"My name is <first_name> <last_name>}"""


def say_my_name(first_name, last_name=""):
    """
    Function to print out the message My name is [<first_name> <last_name>]
    Args:
        first_name: required string argument
        last_name: optional string argument
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
