#!/usr/bin/python3
"""
module for appending text to file
"""


def append_write(filename="", text=""):
    """
    adds text to the end of the file
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
