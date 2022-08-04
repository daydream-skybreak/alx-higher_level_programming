#!/usr/bin/python3
""" the test file for the base.py file """
import unittest
from math import pi
from models.base import Base

class TestBase(unittest.TestCase):
    """class to test the class `Base`"""

    def test_empty(self):
        """ to test object with no arguments"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b2.id - 1)
        self.assertEqual(b1.id, b3.id - 2)

    def test_arg(self):
        """testing when one of the objects has an argument """
        b1 = Base()
        b2 = Base(9)
        b3 = Base()
        self.assertEqual(b2.id, 9)
        self.assertEqual(b1.id, b3.id - 1)

    def test_arg_None(self):
        """ testing when the argument is None """
        b1 = Base(None)
        b2 = Base(None)
        b3 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)
        self.assertEqual(b1.id, b3.id - 2)

    def test_arg_int(self):
        """ testing when the argument is integer """
        self.assertEqual(Base(10).id, 10)

    def test_arg_float(self):
        """ testing when the argument is float """
        self.assertAlmostEqual(Base(pi).id, pi)

    def test_arg_str(self):
        """ testing when the argument is string """
        self.assertEqual(Base("string").id, "string")

    def test_arg_list(self):
        """ testing when the argument is list """
        self.assertEqual(Base([1,2]).id, [1,2])

if __name__ == '__main__':
    unittest.main()
