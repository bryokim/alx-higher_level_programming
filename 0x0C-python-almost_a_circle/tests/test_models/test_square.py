#!/usr/bin/python3
"""
Test module for the Square class.
"""

import unittest
import json
import os

from models.square import Square


class TestSquare(unittest.TestCase):
    def setUp(self):
        """Setup variables used in testing"""
        self.s1 = Square(1, 2, 3, 4)

    def test_valid_values(self):
        """
        Test instanciation of a Square instance with valid
        values for size, x, y, and id.
        """
        self.assertTrue(Square(1))
        self.assertTrue(Square(123, 5))
        self.assertTrue(Square(144, 12, 31))
        self.assertTrue(Square(100, 2, 32, 400))

    def test_missing_argument(self):
        """Test for missing argument"""
        with self.assertRaises(TypeError):
            Square()

    def test_float_size(self):
        """Test for assigning float size"""
        with self.assertRaises(TypeError):
            Square(1.2)

    def test_str_size(self):
        """Test for assigning str size"""
        with self.assertRaises(TypeError):
            Square("1")

    def test_tuple_size(self):
        """Test for assigning tuple size"""
        with self.assertRaises(TypeError):
            Square((1,))

    def test_list_size(self):
        """Test for assigning list size"""
        with self.assertRaises(TypeError):
            Square([2])

    def test_set_size(self):
        """Test for assigning set size"""
        with self.assertRaises(TypeError):
            Square({1})

    def test_zero_size(self):
        """Test for assigning zero as size"""
        with self.assertRaises(ValueError):
            Square(0)

    def test_negative_size(self):
        """Test for assigning negative value as size"""
        with self.assertRaises(ValueError):
            Square(-1)

    def test_float_x_y(self):
        """Test for assigning float x or y."""
        with self.assertRaises(TypeError):
            Square(1, 3.4, 4)
        with self.assertRaises(TypeError):
            Square(1, 3, 4.3)

    def test_str_x_y(self):
        """Test for assigning str x or y."""
        with self.assertRaises(TypeError):
            Square(1, "three", 4)
        with self.assertRaises(TypeError):
            Square(1, 3, "four")

    def test_list_x_y(self):
        """Test for assigning list x or y."""
        with self.assertRaises(TypeError):
            Square(1, [2], 4)
        with self.assertRaises(TypeError):
            Square(1, 3, [])

    def test_tuple_x_y(self):
        """Test for assigning tuple x or y."""
        with self.assertRaises(TypeError):
            Square(1, (3, 4), 4)
        with self.assertRaises(TypeError):
            Square(1, 3, (4,))

    def test_dict_x_y(self):
        """Test for assigning dict x or y."""
        with self.assertRaises(TypeError):
            Square(1, {}, 4)
        with self.assertRaises(TypeError):
            Square(1, 3, {'y': 4})

    def test_negative_x_y(self):
        """Test for assigning negative x or y."""
        with self.assertRaises(ValueError):
            Square(1, -3, 4)
        with self.assertRaises(ValueError):
            Square(1, 3, -4)

    def test_size_getter_and_setter(self):
        """Test for the size getter and setter"""
        self.s1.size = 100
        self.assertEqual(self.s1.size, 100)

    def test_x_getter_and_setter(self):
        """Test for the x getter and setter"""
        self.s1.x = 100
        self.assertEqual(self.s1.x, 100)

    def test_y_getter_and_setter(self):
        """Test for the y getter and setter"""
        self.s1.y = 200
        self.assertEqual(self.s1.y, 200)

    def test_width_equal_to_height(self):
        """Test for equality of height and width"""
        self.s1.size = 200
        self.assertEqual(self.s1.width, self.s1.height)

    def test_area_method(self):
        """Test the area method"""
        self.assertEqual(self.s1.area(), 1)
        self.s1.size = 10
        self.assertEqual(self.s1.area(), 100)
        self.s1.size = 232
        self.assertEqual(self.s1.area(), 232*232)

    def test_str_method(self):
        """Test the __str__ method"""
        string = "[Square] ({}) {}/{} - {}".format(
            self.s1.id, self.s1.x, self.s1.y, self.s1.width
        )
        self.assertEqual(str(self.s1), string)

    def __update_assert_loop(self, values):
        """Loop for checking attributes after updating"""
        for attr, arg in values:
            with self.subTest(attr=attr, arg=arg):
                self.assertEqual(getattr(self.s1, attr), arg)

    def test_update_method(self):
        """Test the update method"""
        attrs = ['id', 'size', 'x', 'y']
        kwargs = {'y': 100, 'x': 20, 'size': 15, 'id': 1}
        args = (7, 8, 45, 23)

        # Test with *args only
        self.s1.update(*args)
        self.__update_assert_loop(zip(attrs, args))

        self.s1.update(23, 4, 5)
        self.__update_assert_loop(zip(attrs, (23, 4, 5)))

        # Test with **kwargs only
        self.s1.update(**kwargs)
        self.__update_assert_loop(kwargs.items())

        self.s1.update(size=90, id=9, x=12)
        self.__update_assert_loop(zip(["size", "id", "x"], [90, 9, 12]))

        # Test with both *ags and **kwargs
        args = (1, 23, 43, 89)
        self.s1.update(*args, **kwargs)
        self.__update_assert_loop(zip(attrs, args))

        # Test with new attributes.
        kwargs = {'name': 'square1', 'age': 21}
        self.s1.update(**kwargs)
        self.assertEqual(getattr(self.s1, 'name'), "square1")
        self.assertEqual(getattr(self.s1, 'age'), 21)

        # Test with invalid values
        invalid_args = [1, 2, 'three']
        with self.assertRaises(TypeError):
            self.s1.update(*invalid_args)

        invalid_kwargs = {'size': 0, 'x': 10, 'y': 20}
        with self.assertRaises(ValueError):
            self.s1.update(**invalid_kwargs)

    def test_to_dictionary_method(self):
        """Test the to_dictionary method"""
        dictionary = {
            'id': self.s1.id,
            'size': self.s1.size,
            'x': self.s1.x,
            'y': self.s1.y,
        }
        for key, value in self.s1.to_dictionary().items():
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
        squares = [Square(i) for i in range(1, num + 1)]
        square_dicts = [Square.to_dictionary(rect) for rect in squares]
        return (Square.to_json_string(square_dicts), square_dicts)

    def test_to_json_string_method(self):
        """Test the to_json_string method."""
        # Test an empty list.
        self.assertEqual(Square.to_json_string([]), "[]")

        # Test with one dictionary.
        json_string, square_dict = self.__create_dicts_and_json_strings()
        self.assertEqual(json_string, json.dumps(square_dict))

        # Test with several dictionaries.
        json_string, square_dicts = self.__create_dicts_and_json_strings(5)
        self.assertEqual(json_string, json.dumps(square_dicts))

    def test_from_json_string_method(self):
        """Test the from_json_string method"""
        # Test with empty string.
        self.assertEqual(Square.from_json_string(""), [])

        # Test with string containing single dictionary.
        json_string, square_dict = self.__create_dicts_and_json_strings()
        list_dict = Square.from_json_string(json_string)
        self.assertEqual(list_dict, square_dict)

        # Test with string containing several dictionries.
        json_string, square_dicts = self.__create_dicts_and_json_strings(5)
        list_dicts = Square.from_json_string(json_string)
        self.assertEqual(list_dicts, square_dicts)

    @staticmethod
    def __create_list_of_squares_and_save(num=1):
        """
        Returns a list of Square instances that have been saved to a file.

        Args:
            num (int, optional): Number of square instances. Defaults to 1.

        Returns:
            list: A list of Square instances.
        """
        list_squares = [Square(i) for i in range(1, num + 1)]
        Square.save_to_file(list_squares)

        return list_squares

    def test_save_to_file_method(self):
        """Test the save to file method."""

        list_squares = self.__create_list_of_squares_and_save(5)
        with open("Square.json", "r") as f:
            data = json.load(f)
        list_square_dicts = [square.to_dictionary() for square in list_squares]
        self.assertEqual(list_square_dicts, data)
        os.remove("Square.json")

    def test_load_from_file(self):
        """Test the load_from_file method"""

        # Test loading from available file.
        list_squares = self.__create_list_of_squares_and_save(5)
        loaded_squares = Square.load_from_file()

        for loaded, old in zip(loaded_squares, list_squares):
            self.assertTrue(type(loaded) is Square)
            for attr in ["id", "size", "x", "y"]:
                self.assertEqual(getattr(loaded, attr), getattr(old, attr))
        os.remove("Square.json")

        # Test loading from unvailable file.
        loaded_squares = Square.load_from_file()
        self.assertEqual(loaded_squares, [])

    def test_create_method(self):
        """Test the create method"""

        values = {'id': 13, 'size': 2, 'x': 0, 'y': 9}
        new_square = Square.create(**values)

        self.assertTrue(type(new_square) is Square)
        for key, value in values.items():
            self.assertEqual(getattr(new_square, key), value)


if __name__ == "__main__":
    unittest.main()
