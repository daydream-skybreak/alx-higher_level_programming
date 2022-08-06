#!/usr/bin/python3
"""square representation"""

try:
    from models.rectangle import Rectangle
except Exception:
    from rectangle import Rectangle


class Square(Rectangle):
    """class for square representation"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        initialization of  the square
        Args:
            size: size of the square
            x: x coordinate of the square (default=0)
            y: y coordinate of the square (default=0)
            id: id of the square (default=0)
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get and set the size of the square"""
        return self.width

    @size.setter
    def size(self, val):
        self.width = val
        self.height = val

    def __str__(self):
        """ returns the string representation of the square """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
