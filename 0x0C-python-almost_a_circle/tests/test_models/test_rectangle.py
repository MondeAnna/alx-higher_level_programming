#!/usr/bin/python3


""" Test Rectangle
"""


from unittest.mock import mock_open
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

    @patch("builtins.print")
    def test_display_rectangle_include_x(self, mock_print):
        Rectangle(1, 2, 3).display()

        self.assertEqual(mock_print.call_count, 2)
        mock_print.assert_called_with("   #")

    @patch("builtins.print")
    def test_display_rectangle_include_y(self, mock_print):
        Rectangle(10, 5, 0, 3).display()

        print_out = self.get_mock_print(mock_print)

        self.assertTrue("\\n\\n\\n" in print_out)
        mock_print.assert_called_with("##########")
        self.assertEqual(mock_print.call_count, 6)

    @patch("builtins.print")
    def test_display_rectangle_include_x_and_y(self, mock_print):
        Rectangle(3, 9, 2, 3).display()

        print_out = self.get_mock_print(mock_print)

        self.assertTrue("\\n\\n\\n" in print_out)
        mock_print.assert_called_with("  ###")
        self.assertEqual(mock_print.call_count, 10)


class TestInstancePrintOut(TestRectangle):

    """ Test Print out of Rectangle instance
    """

    @patch("builtins.print")
    def test_display_str_representation(self, mock_print):
        rectangle_01 = Rectangle(4, 6, 2, 1, 12)
        rectangle_02 = Rectangle(5, 5, 1)

        print(rectangle_01)
        print(rectangle_02)

        expected_01 = "[Rectangle] (12) 2/1 - 4/6"
        expected_02 = "[Rectangle] (1) 1/0 - 5/5"

        print_out = self.get_mock_print(mock_print)

        self.assertTrue(expected_01 in print_out)
        self.assertTrue(expected_02 in print_out)
        self.assertEqual(mock_print.call_count, 2)


class TestUpdate(TestRectangle):

    """ Test attribute update of Rectangle instance
    """

    @patch("builtins.print")
    def test_update_no_args_or_kwargs(self, mock_print):
        expected = "[Rectangle] (1) 2/22 - 98/3"

        rectangle = Rectangle(98, 3, 2, 22)
        print(rectangle)

        print_out = self.get_mock_print(mock_print)
        self.assertTrue(expected in print_out)

        mock_print.reset_mock()
        rectangle.update()

        self.assertTrue(expected in print_out)

    @patch("builtins.print")
    def test_update_with_args(self, mock_print):
        cases = (
            ((89,), "[Rectangle] (89) 10/10 - 10/10"),
            ((89, 2), "[Rectangle] (89) 10/10 - 2/10"),
            ((89, 2, 3), "[Rectangle] (89) 10/10 - 2/3"),
            ((89, 2, 3, 4), "[Rectangle] (89) 4/10 - 2/3"),
            ((89, 2, 3, 4, 5), "[Rectangle] (89) 4/5 - 2/3"),
        )

        rectangle = Rectangle(10, 10, 10, 10)

        for args, expected in cases:
            rectangle.update(*args)
            print(rectangle)

            print_out = self.get_mock_print(mock_print)
            self.assertTrue(expected in print_out)

            mock_print.reset_mock()

    @patch("builtins.print")
    def test_update_with_kwargs(self, mock_print):
        rectangle = Rectangle(10, 10, 10, 10)

        cases = (
            ({"height": 1}, "[Rectangle] (1) 10/10 - 10/1"),
            ({"width": 1, "x": 2}, "[Rectangle] (1) 2/10 - 1/1"),
            (
                {"y": 1, "width": 2, "x": 3, "id": 89},
                "[Rectangle] (89) 3/1 - 2/1",
            ),
            (
                {"x": 1, "height": 2, "y": 3, "width": 4},
                "[Rectangle] (89) 1/3 - 4/2",
            ),
        )

        for kargs, expected in cases:
            rectangle.update(**kargs)
            print(rectangle)

            print_out = self.get_mock_print(mock_print)
            self.assertTrue(expected in print_out)

            mock_print.reset_mock()


class TestToDictionary(TestRectangle):

    """ Test returning attribute-value pairs as a dictionary
    """

    def test_to_dict(self):
        result = Rectangle(10, 2, 1, 9).to_dictionary()
        expected = {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9}
        self.assertEqual(result, expected)


class TestSaveToFile(TestRectangle):

    """ Write JSON String to file
    """

    @patch("builtins.open", new_callable=mock_open())
    def test_list_of_rectangles(self, mock_open):
        Base.save_to_file([Rectangle(10, 7, 2, 8), Rectangle(2, 4)])

        dict_01 = '{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}'
        dict_02 = '{"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}'
        expected = f"[{dict_01}, {dict_02}]"
        filename = "Rectangle.json"

        mock_open.assert_called_once_with(filename, "w", encoding="utf-8")
        mock_open().__enter__().write.assert_called_once_with(expected)


class TestCreate(TestRectangle):

    """ Test factory method
    """

    def test_create(self):
        kwargs = {"width": 1, "height": 2, "x": 1, "y": 0}
        rectangle = Rectangle.create(**kwargs)

        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 1)
        self.assertEqual(rectangle.y, 0)


if __name__ == "__main__":
    unittest.main()
