#!/usr/bin/python3
"""A function that prints and returns the last digit of a number"""

def print_last_digit(number):
    if number >= 0:
        print(number % 10, end="")
        return number % 10
    else:
        print((-1 * number) % 10, end="")
        return (-1 * number) % 10
