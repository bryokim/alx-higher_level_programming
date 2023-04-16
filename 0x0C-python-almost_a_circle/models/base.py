#!/usr/bin/python3
"""
Iplementation of the Base class
"""
import json


class Base:
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
