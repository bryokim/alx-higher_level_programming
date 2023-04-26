#!/usr/bin/python3
"""
Iplementation of the Base class
"""
import json
import csv
import sys
import turtle


class Base:
    """Base Class implementation."""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base instance.

        Args:
            id (int, optional): The id of the instance. Defaults to None.
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): List of dictionries.

        Returns:
            str: List of JSON string representations, or "[]" if
                 list_dictionaries is None or empty.
        """
        if not list_dictionaries:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Filename is always <Class name>.json

        Args:
            list_objs (list): List of instances that inherit from Base.
        """
        list_dictionaries = [cls.to_dictionary(obj) for obj in list_objs]
        filename = f"{cls.__name__}.json"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string.

        Args:
            json_string (str): string representing a list of dictionaries.

        Returns:
            list: A list represented by json_string, or an empty list
                  if json_string is None or empty.
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all atributes already set.

        Args:
            dictionary (dict): Dictionary containing attribute and
                    value pairs.

        Returns:
            object: New instance of the class with attributes set using
                dictionary.
        """
        if cls.__name__ == "Square":
            obj = cls(1)
        else:
            obj = cls(1, 1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances.

        Filename must be <Class name>.json

        Returns:
            list: List of instances depending on cls(current class
                    using method).
        """
        try:
            filename = f"{cls.__name__}.json"
            with open(filename, "r") as f:
                json_string = f.read()
        except FileNotFoundError:
            return []
        list_dicts = cls.from_json_string(json_string)
        return [cls.create(**dictionary) for dictionary in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serealizes in csv.

        Args:
            list_objs (list): List of instances.
        """
        list_dictionaries = [cls.to_dictionary(obj) for obj in list_objs]
        filename = f"{cls.__name__}.csv"
        if cls.__name__ == "Square":
            fields = ["id", "size", "x", "y"]
        else:
            fields = ["id", "width", "height", "x", "y"]
        with open(filename, "w") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(list_dictionaries)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes in csv.
        Exits if one of th values being read is not an integer
        """
        try:
            filename = f"{cls.__name__}.csv"
            with open(filename) as csv_file:
                reader = csv.DictReader(csv_file)
                loaded_dicts = []
                for dictionary in reader:
                    for key, value in dictionary.items():
                        try:
                            dictionary[key] = int(value)
                        except ValueError:
                            sys.exit(f"{key} must be an integer.\
Line on csv file: {reader.line_num}")
                    loaded_dicts.append(dictionary)
                return [cls.create(**dict) for dict in loaded_dicts]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the rectangles and squares.

        Args:
            list_rectangles (list): List of rectangles.
            list_squares (list): List of squares.
        """
        wn = turtle.Screen()
        wn.bgcolor("light blue")
        wn.title("Rectangles and squares")
        t = turtle.Turtle()
        t.pencolor("black")
        t.pensize(4)
        t.penup()

        for rect in list_rectangles:
            t.goto(rect.x, rect.y)
            t.pendown()
            for i in range(2):
                t.fd(rect.width)
                t.left(90)
                t.fd(rect.height)
                t.left(90)
            t.penup()

        for square in list_squares:
            t.goto(square.x, square.y)
            t.pendown()
            for i in range(4):
                t.fd(square.size)
                t.left(90)
            t.penup()

        turtle.done()
