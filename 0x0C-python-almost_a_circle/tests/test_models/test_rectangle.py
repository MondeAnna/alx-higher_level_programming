#!/usr/bin/python3


""" Test Rectangle
"""


from unittest.mock import patch
import unittest


from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):

    """ Universally applied, cross test methods
    """

    def setUp(self):
        self.__nb_objects = Base._Base__nb_objects

    def tearDown(self):
        Base._Base__nb_objects = self.__nb_objects

    @staticmethod
    def get_mock_print(mock_print):
        calls = mock_print.call_args_list
        return " ".join(
            str(call_.args)
            for call_ in calls
        )


class TestInitialisation(TestRectangle):

    """ Test Rectangle Initialisation
    """

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

    def test_init_with_id(self):
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


class TestRectangleValidity(TestRectangle):

    """ Test Rectangle Validity
    """

    def test_raise_if_attr_not_int(self):
        kwargs_and_errors = (
            ({"width": 4.5, "height": 6}, "width must be an integer"),
            ({"width": 3, "height": 7.8}, "height must be an integer"),
            ({"width": 2, "height": 9, "x": 12.13}, "x must be an integer"),
            (
                {"width": 1, "height": 10, "x": 11, "y": 14.15},
                "y must be an integer",
            ),
        )

        for kwargs, error in kwargs_and_errors:
            with self.assertRaises(TypeError) as exception:
                Rectangle(**kwargs)
            self.assertEqual(str(exception.exception), error)

    def test_raise_if_attr_not_positive(self):
        kwargs_and_errors = (
            ({"width": 0, "height": 6}, "width must be > 0"),
            ({"width": 3, "height": -1}, "height must be > 0"),
        )

        for kwargs, error in kwargs_and_errors:
            with self.assertRaises(ValueError) as exception:
                Rectangle(**kwargs)
            self.assertEqual(str(exception.exception), error)

    def test_raise_if_attr_negative(self):
        kwargs_and_errors = (
            ({"width": 1, "height": 2, "x": -1, "y": 0}, "x must be >= 0"),
            ({"width": 1, "height": 2, "x": 0, "y": -1}, "y must be >= 0"),
        )

        for kwargs, error in kwargs_and_errors:
            with self.assertRaises(ValueError) as exception:
                Rectangle(**kwargs)
            self.assertEqual(str(exception.exception), error)


class TestArea(TestRectangle):

    """ Test Rectangle Area
    """

    def test_area(self):
        rectangles = (
            (Rectangle(3, 2), 6),
            (Rectangle(2, 10), 20),
            (Rectangle(8, 7, 0, 0, 12), 56),
        )

        for rectangle, expected in rectangles:
            self.assertEqual(rectangle.area(), expected)


class TestDisplay(TestRectangle):

    """ Test Rectangle's Output to stdout
    """

    @patch("builtins.print")
    def test_display_rectangle(self, mock_print):
        Rectangle(4, 6).display()

        print_out = self.get_mock_print(mock_print)

        mock_print.assert_called_with("####")
        self.assertEqual(mock_print.call_count, 6)


if __name__ == "__main__":
    unittest.main()
