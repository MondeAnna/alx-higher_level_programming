#!/usr/bin/python3


""" Test Rectangle
"""


import unittest


from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):

    """ Test Rectangle
    """

    def setUp(self):
        self.__nb_objects = Base._Base__nb_objects

    def tearDown(self):
        Base._Base__nb_objects = self.__nb_objects

    def test_instance_attr_no_id(self):
        rectangle = Rectangle(
            width=100,
            height=200,
            x=0,
            y=0,
        )

        self.assertEqual(rectangle.width, 100)
        self.assertEqual(rectangle.height, 200)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)
        self.assertEqual(rectangle.id, 1)

    def test_instance_attr_with_id(self):
        rectangle = Rectangle(
            width=33,
            height=55,
            x=18,
            y=12,
            id=23
        )

        self.assertEqual(rectangle.width, 33)
        self.assertEqual(rectangle.height, 55)
        self.assertEqual(rectangle.x, 18)
        self.assertEqual(rectangle.y, 12)
        self.assertEqual(rectangle.id, 23)

    def test_inheritance_of_id_logic(self):
        rectangles = (
            (Rectangle(10, 2), 1),
            (Rectangle(2, 10), 2),
            (Rectangle(11, 12, 0, 0, 12), 12),
        )

        for rectangle, expected in rectangles:
            self.assertEqual(rectangle.id, expected)


if __name__ == "__main__":
    unittest.main()
