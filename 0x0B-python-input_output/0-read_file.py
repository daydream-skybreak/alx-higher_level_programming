#!/usr/bin/python3
""" module for reading a file """


def read_file(filename=""):
    with open(filename) as f:
        for line in f:
            print(line, end="")
