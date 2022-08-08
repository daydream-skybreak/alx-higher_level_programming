#!/usr/bin/python3
"""
Base class instantiation module
"""

import random
import json
import csv
import turtle


class Base:
    """base class for all the other classes in this project"""
    __nb_object = 0

    def __init__(self, id=None):
        """ instantiation function
        Args:
            id: id of instances
        """
        if id is None:
            Base.__nb_object += 1
            self.id = Base.__nb_object
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON Serialization of a list of dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """that writes the JSON string representation of list_objs to a file
        Args:
            list_objs: list of objects of a certain class
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dict = [ob.to_dictionary() for ob in list_objs]
                file.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of deserialized the JSON string
        Args:
            json_string: as the name suggests
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dumy = cls(1, 1)
        else:
            dumy = cls(1)
        dumy.update(**dictionary)
        return dumy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a .json file
        Returns an empty list if the file doesn't exist
        Reads from => <class.__name__>.json
        """
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, "r") as file:
                list_dict = Base.from_json_string(file.read())
                return [cls.create(**d) for d in list_dict]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        Reads from `<cls.__name__>.csv`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draws the list of rectangles and squares on turtle graphics

        Args:
            list_rectangles=> list of rectangle instances
            list_squares=> list of square instances
        """
        scr = turtle.Screen()
        tur = turtle.Turtle()
        tur.pen()
        tur.hideturtle()
        tur.speed(6)
        for rect in list_rectangles:
            a, b, c = [random.randint(1, 255) for i in range(3)]
            tur.color(a / 255, b / 255, c / 255)
            tur.penup()
            tur.setpos(rect.x, rect.y)
            for i in range(2):
                tur.pendown()
                tur.fd(rect.width)
                tur.rt(90)
                tur.fd(rect.height)
                tur.rt(90)
            tur.fillcolor(colors[random.randint(0, len(colors) - 1)])

        for sqr in list_squares:
            tur.penup()
            tur.setpos(sqr.x, sqr.y)
            tur.color(colors[random.randint(0, len(colors) - 1)])
            a, b, c = [random.randint(1, 255) for i in range(3)]
            tur.color(a / 255, b / 255, c / 255)
            for i in range(4):
                tur.pendown()
                tur.fd(sqr.size)
                tur.rt(90)
        while True:
            scr.update()
