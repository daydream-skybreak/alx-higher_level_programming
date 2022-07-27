#!/usr/bin/python3
""" a file to create a frozen class """


class LockedClass:
    """this is a locked class th only take attribute <first_name> """

    __slots__ = ["first_name"]
