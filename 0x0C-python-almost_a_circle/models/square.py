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

    def update(self, *args, **kwargs):
        """method to update the values of the square instance
        order of argument for args:
            (1): id
            (2): size
            (3): x
            (4): y
        """
        if args and len(args) != 0:
            idx = 0
            for val in args:
                if idx == 0:
                    if idx is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = val
                elif idx == 1:
                    self.size = val
                elif idx == 2:
                    self.x = val
                elif idx == 3:
                    self.y = val
                idx += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns dictionary representation representation of the instance"""
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "size": self.width
        }

    def __str__(self):
        """ returns the string representation of the square """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
