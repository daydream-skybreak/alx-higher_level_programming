#!/usr/bin/python3
""" 
module for writing on files
"""


def write_file(filename="", text=""):
    """
    writes to a file
    creates file if it doesn't exist
    over-writes whatever is on the file
    """
    with open(filename, 'w+', encoding="utf-8") as f:
        return f.write(text)
