#!/usr/bin/python3
import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    def setUp(self):
        self.int_list = [1, 2, 3, 4, 5]
        self.float_list = [10.3, 4.5, 3.2, 4.3, 9.5]
        self.str_list = ["one", "two", "three"]
        self.mixed_list = [1, 2, "0ne", "two"]

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_int_list(self):
        self.assertEqual(max_integer(self.int_list), 5)

    def test_float_list(self):
        self.assertEqual(max_integer(self.float_list), 10.3)

    def test_mixed_list(self):
        with self.assertRaises(TypeError):
            max = max_integer(self.mixed_list)

    def test_str_list(self):
        self.assertEqual(max_integer(self.str_list), "two")

    def test_not_list(self):
        with self.assertRaises(TypeError):
            max = max_integer(1)
