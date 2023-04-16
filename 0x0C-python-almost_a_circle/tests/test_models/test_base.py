#!/usr/bin/python3

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_with_id(self):
        base = Base(22)
        self.assertEqual(base.id, 22)

    def test_no_id(self):
        base = Base()
        self.assertEqual(base.id, 4)

    def test_multiple_ids(self):
        bases = [Base(12)]
        bases.extend([Base() for i in range(3)])
        bases.append(Base(23))

        for id, base in enumerate(bases):
            if id == 0:
                id = 12
            elif id == 4:
                id = 23
            with self.subTest(id=id):
                self.assertEqual(id, base.id)


if __name__ == "__main__":
    unittest.main()
