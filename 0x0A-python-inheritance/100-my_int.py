#!/usr/bin/python3
"""
module that inverts the operations == and !=
"""


class MyInt(int):
    """ class inheriting from int and swapping == with != """
    def __eq__(self, value):
        """equality reversed"""
        return self.real != value

    def __ne__(self, value):
        """ inequality reversed"""
        return self.real == value
