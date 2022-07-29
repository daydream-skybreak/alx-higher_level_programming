#!/usr/bin/python3
""" module containing:
        print_square: prints square using character '#'
"""


def print_square(size):
    """
    a function to print square using '#'
    Args:
        size: size of the square
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        [print('#', end='') for j in range(size)]
        print('')
