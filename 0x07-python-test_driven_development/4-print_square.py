#!/usr/bin/python3
""" module containing:
        print_square: prints square using character '#'
"""


def print_square(size):
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    print('\n'.join(['#' * size for i in range(size)]))
