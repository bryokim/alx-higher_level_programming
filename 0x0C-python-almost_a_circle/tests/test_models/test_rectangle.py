#!/usr/bin/python3
"""
Test module for the Rectangle class
"""

import unittest
import json
import os

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """TestRectangle class. Inherits from unittest.TestCase."""

    def setUp(self):
        """Setup variables used in testing."""
        self.r1 = Rectangle(1, 2, 3, 4, 5)

    def test_valid_values(self):
        """
        Test instanciation of a Rectangle instance with valid
        values for width, height, x, y, and id.
        """
        self.assertTrue(Rectangle(1, 2))
        self.assertTrue(Rectangle(1, 2, 3))
        self.assertTrue(Rectangle(1, 2, 3, 4))
        self.assertTrue(Rectangle(1, 2, 3, 4, 5))

    def test_missing_argument(self):
        """Test for missing argument(s)."""
        with self.assertRaises(TypeError):
            Rectangle(1)
        with self.assertRaises(TypeError):
            Rectangle()

    def test_float_width_height(self):
        """Test for assigning float width or height."""
        with self.assertRaises(TypeError):
            Rectangle(1.1, 2)
        with self.assertRaises(TypeError):
            Rectangle(1, 2.1)

    def test_str_width_height(self):
        """Test for assigning str width or height."""
        with self.assertRaises(TypeError):
            Rectangle("one", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "two")

    def test_tuple_width_height(self):
        """Test for assigning tuple width or height."""
        with self.assertRaises(TypeError):
            Rectangle((1,), 2)
        with self.assertRaises(TypeError):
            Rectangle(1, (2,))

    def test_list_width_height(self):
        """Test for assigning list width or height."""
        with self.assertRaises(TypeError):
            Rectangle([1], 2)
        with self.assertRaises(TypeError):
            Rectangle(1, [2])

    def test_dict_width_height(self):
        """Test for assigning dict width or height."""
        with self.assertRaises(TypeError):
            Rectangle({'width': 1}, 2)
        with self.assertRaises(TypeError):
            Rectangle(1, {})

    def test_zero_width_height(self):
        """Test for assigning zero as width or height."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_negative_width_height(self):
        """Test for assigning negative width or height."""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_float_x_y(self):
        """Test for assigning float x or y."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3.4, 4)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4.3)

    def test_str_x_y(self):
        """Test for assigning str x or y."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "three", 4)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "four")

    def test_list_x_y(self):
        """Test for assigning list x or y."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, [], 4)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, [])

    def test_tuple_x_y(self):
        """Test for assigning tuple x or y."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, (3, 4), 4)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, (4,))

    def test_dict_x_y(self):
        """Test for assigning dict x or y."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, {}, 4)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, {'y': 4})

    def test_negative_x_y(self):
        """Test for assigning negative x or y."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3, 4)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_width_getter_and__setter(self):
        """Test for the width getter and setter"""
        self.r1.width = 3
        self.assertEqual(self.r1.width, 3)

    def test_height_getter_and_setter(self):
        """Test for the height getter and setter"""
        self.r1.height = 4
        self.assertEqual(self.r1.height, 4)

    def test_x_getter_and_setter(self):
        """Test for the x getter and setter"""
        self.r1.x = 100
        self.assertEqual(self.r1.x, 100)

    def test_y_getter_and_setter(self):
        """Test for the y getter and setter"""
        self.r1.y = 200
        self.assertEqual(self.r1.y, 200)

    def test_area_method(self):
        """Test the area method"""
        self.assertEqual(self.r1.area(), 2)
        self.r1.width = 10
        self.assertEqual(self.r1.area(), 20)
        self.r1.height = 232
        self.assertEqual(self.r1.area(), 2320)

    def test_str_method(self):
        """Test the __str__ method"""
        string = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.r1.id, self.r1.x, self.r1.y, self.r1.width, self.r1.height
        )
        self.assertEqual(str(self.r1), string)

    def __update_assert_loop(self, values):
        """Loop for checking attributes after updating"""
        for attr, arg in values:
            with self.subTest(attr=attr, arg=arg):
                self.assertEqual(getattr(self.r1, attr), arg)

    def test_update_method(self):
        """Test the update method"""
        attrs = ["id", "width", "height", "x", "y"]
        kwargs = {'x': 10, 'height': 20, 'id': 2, 'width': 30, 'y': 3}
        args = [10, 20, 30, 2, 3]

        # Test with *args only.
        self.r1.update(*args)
        self.__update_assert_loop(zip(attrs, args))

        self.r1.update(99, 23, 22)
        self.__update_assert_loop(zip(attrs, [99, 23, 22]))

        # Test with *args exceeding required arguments.
        args = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.r1.update(*args)
        self.__update_assert_loop(zip(attrs, args))

        # Test with **kwargs only.
        self.r1.update(**kwargs)
        self.__update_assert_loop(kwargs.items())

        self.r1.update(id=23, width=150, x=99)
        self.__update_assert_loop(zip(["id", "width", "x"], [23, 150, 99]))

        # Test with both *args and **kwargs
        self.r1.update(*args, **kwargs)
        self.__update_assert_loop(zip(attrs, args))

        # Test with new attributes.
        kwargs = {'id': 10, 'y': 2, 'name': 'Brian', 'x': 20}
        self.r1.update(**kwargs)
        self.assertEqual(self.r1.name, 'Brian')

        # Test with invalid values.
        invalid_args = [1, 2, "3", []]
        with self.assertRaises(TypeError):
            self.r1.update(*invalid_args)

        invalid_kwargs = {'id': 20, 'width': 0, 'x': 0}
        with self.assertRaises(ValueError):
            self.r1.update(**invalid_kwargs)

    def test_to_dictionary_method(self):
        """Test the to_dictionary method"""
        dictionary = {
            'id': self.r1.id,
            'width': self.r1.width,
            'height': self.r1.height,
            'x': self.r1.x,
            'y': self.r1.y,
        }
        for key, value in self.r1.to_dictionary().items():
            self.assertEqual(value, dictionary[key])

    @staticmethod
    def __create_dicts_and_json_strings(num=1):
        """
        Create dictionary and json strings.

        Args:
            num (int, optional): Number of dictionaries and json strings
             to create.

        Returns:
            tuple: A tuple of json strings and respctive dictionaries.
        """
        rects = [Rectangle(1, 2) for i in range(num)]
        rects_dicts = [Rectangle.to_dictionary(rect) for rect in rects]
        return (Rectangle.to_json_string(rects_dicts), rects_dicts)

    def test_to_json_string_method(self):
        """Test to_json_string method"""
        # Test with empty list.
        self.assertEqual(Rectangle.to_json_string([]), "[]")

        # Test with one dictionary.
        json_string, rect_dict = self.__create_dicts_and_json_strings()
        self.assertEqual(json_string, json.dumps(rect_dict))

        # Test with several dictionaries.
        json_strings, rect_dicts = self.__create_dicts_and_json_strings(5)
        self.assertEqual(json_strings, json.dumps(rect_dicts))

    def test_from_json_string_method(self):
        """Test the from_json_string method."""
        # Test with empty string.
        self.assertEqual(Rectangle.from_json_string(""), [])

        # Test with string containing single dictionary.
        json_string, rect_dicts = self.__create_dicts_and_json_strings()
        list_dicts = Rectangle.from_json_string(json_string)
        self.assertEqual(list_dicts, rect_dicts)

        # Test with string containing multiple dictionaries.
        json_strings, rect_dicts = self.__create_dicts_and_json_strings(5)
        list_dicts = Rectangle.from_json_string(json_strings)
        self.assertEqual(list_dicts, rect_dicts)

    def test_save_to_file_method(self):
        """Test the save_to_file_method."""

        list_rects = [Rectangle(1, 1) for i in range(5)]
        Rectangle.save_to_file(list_rects)
        with open("Rectangle.json", 'r') as f:
            data = json.load(f)
        dict_rects = [rect.to_dictionary() for rect in list_rects]
        self.assertEqual(data, dict_rects)
        os.remove("Rectangle.json")

    def test_load_from_file(self):
        """Test the load_from_file method"""

        # Test loading from available file.
        list_rects = [Rectangle(1, 1) for i in range(5)]
        Rectangle.save_to_file(list_rects)
        loaded_rects = Rectangle.load_from_file()

        for loaded, old in zip(loaded_rects, list_rects):
            self.assertTrue(type(loaded) is Rectangle)
            for attr in ["id", "width", "height", "x", "y"]:
                self.assertEqual(getattr(loaded, attr), getattr(old, attr))
        os.remove("Rectangle.json")

        # Test loading from unavailable file.
        loaded_rects = Rectangle.load_from_file()
        self.assertEqual(loaded_rects, [])

    def test_create_method(self):
        """Test the create method."""

        values = {"id": 23, "width": 2, "height": 6, "x": 9, "y": 8}
        new_rectangle = Rectangle.create(**values)

        self.assertTrue(type(new_rectangle) is Rectangle)
        for key, value in values.items():
            self.assertEqual(getattr(new_rectangle, key), value)


if __name__ == "__main__":
    unittest.main()
