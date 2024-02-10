#!/usr/bin/python3


""" Test Square
"""


from unittest.mock import mock_open
from unittest.mock import patch
import unittest


from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):

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


class TestInitialisation(TestSquare):

    """ Test Square Initialisation
    """

    def test_instance_attr_no_id(self):
        square = Square(
            size=100,
            x=0,
            y=0,
        )

        self.assertEqual(square.area(), 10_000)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertEqual(square.id, 1)

    def test_init_with_id(self):
        square = Square(
            size=33,
            x=18,
            y=12,
            id=23
        )

        self.assertEqual(square.area(), 1_089)
        self.assertEqual(square.x, 18)
        self.assertEqual(square.y, 12)
        self.assertEqual(square.id, 23)

    def test_inheritance_of_id_logic(self):
        squares = (
            (Square(10), 1),
            (Square(2, 10, 0), 2),
            (Square(11, 12, 0, 12), 12),
        )

        for square, expected in squares:
            self.assertEqual(square.id, expected)


class TestSquareValidity(TestSquare):

    """ Test Square Validity
    """

    def test_raise_if_attr_not_int(self):
        kwargs_and_exceptions = (
            ({"size": 4.5}, "width must be an integer"),
            ({"size": 2, "x": 12.13}, "x must be an integer"),
            ({"size": 3, "y": 7.8}, "y must be an integer"),
        )

        for kwargs, exception in kwargs_and_exceptions:
            with self.assertRaises(TypeError) as raised:
                Square(**kwargs)
            self.assertEqual(str(raised.exception), exception)

    def test_raise_if_size_not_positive(self):
        exception = "width must be > 0"
        with self.assertRaises(ValueError) as raised:
            Square(size=-1)
        self.assertEqual(str(raised.exception), exception)

    def test_raise_if_attr_negative(self):
        kwargs_and_exceptions = (
            ({"size": 1, "x": -1, "y": 0}, "x must be >= 0"),
            ({"size": 1, "x": 0, "y": -1}, "y must be >= 0"),
        )

        for kwargs, exception in kwargs_and_exceptions:
            with self.assertRaises(ValueError) as raised:
                Square(**kwargs)
            self.assertEqual(str(raised.exception), exception)


class TestArea(TestSquare):

    """ Test Square Area
    """

    def test_area(self):
        squares = (
            (Square(10), 100),
            (Square(3, 2), 9),
            (Square(8, 7, 0, 12), 64),
        )

        for square, expected in squares:
            self.assertEqual(square.area(), expected)


class TestDisplay(TestSquare):

    """ Test Square's Output to stdout
    """

    @patch("builtins.print")
    def test_display_square(self, mock_print):
        Square(10).display()

        mock_print.assert_called_with("##########")
        self.assertEqual(mock_print.call_count, 10)

    @patch("builtins.print")
    def test_display_square_include_x(self, mock_print):
        Square(4, 6).display()

        mock_print.assert_called_with("      ####")
        self.assertEqual(mock_print.call_count, 4)

    @patch("builtins.print")
    def test_display_square_include_x_and_y(self, mock_print):
        Square(1, 2, 3).display()

        print_out = self.get_mock_print(mock_print)

        self.assertTrue("\\n\\n\\n" in print_out)
        self.assertEqual(mock_print.call_count, 2)
        mock_print.assert_called_with("  #")


class TestInstancePrintOut(TestSquare):

    """ Test Print out of Square instance
    """

    @unittest.skip
    @patch("builtins.print")
    def test_display_str_representation(self, mock_print):
        square_01 = Square(4, 2, 1, 12)
        square_02 = Square(5, 5, 1)

        print(square_01)
        print(square_02)

        expected_01 = "[Square] (12) 2/1 - 4"
        expected_02 = "[Square] (1) 5/1 - 5"

        print_out = self.get_mock_print(mock_print)

        self.assertTrue(expected_01 in print_out)
        self.assertTrue(expected_02 in print_out)
        self.assertEqual(mock_print.call_count, 2)


class TestUpdate(TestSquare):

    """ Test attribute update of Square instance
    """

    @unittest.skip
    @patch("builtins.print")
    def test_update_no_args_or_kwargs(self, mock_print):
        expected = "[Square] (22) 3/2 - 98"

        square = Square(98, 3, 2, 22)
        print(square)

        print_out = self.get_mock_print(mock_print)
        self.assertTrue(expected in print_out)

        mock_print.reset_mock()
        square.update()

        self.assertTrue(expected in print_out)

    @unittest.skip
    @patch("builtins.print")
    def test_update_with_args(self, mock_print):
        cases = (
            ((89,), "[Square] (89) 10/10 - 10"),
            ((89, 2), "[Square] (89) 10/10 - 2"),
            ((89, 2, 3), "[Square] (89) 3/10 - 2"),
            ((89, 2, 3, 4), "[Square] (89) 3/4 - 2"),
        )

        square = Square(10, 10, 10, 10)

        for args, expected in cases:
            square.update(*args)
            print(square)

            print_out = self.get_mock_print(mock_print)
            self.assertTrue(expected in print_out)

            mock_print.reset_mock()

    @unittest.skip
    @patch("builtins.print")
    def test_update_with_kwargs(self, mock_print):
        square = Square(10, 10, 10, 10)

        cases = (
            ({"size": 1}, "[Square] (10) 10/10 - 1"),
            ({"id": 13, "x": 2}, "[Square] (13) 2/10 - 1"),
            ({"y": 1, "x": 3, "id": 89}, "[Square] (89) 3/1 - 1"),
        )

        for kargs, expected in cases:
            square.update(**kargs)
            print(square)

            print_out = self.get_mock_print(mock_print)
            self.assertTrue(expected in print_out)

            mock_print.reset_mock()


class TestToDictionary(TestSquare):

    """ Test returning attribute-value pairs as a dictionary
    """

    def test_to_dict(self):
        result = Square(10, 2, 1, 9).to_dictionary()
        expected = {"id": 9, "size": 10, "x": 2, "y": 1}
        self.assertEqual(result, expected)


class TestSaveToFile(TestSquare):

    """ Write JSON String to file
    """

    @patch("builtins.open", new_callable=mock_open())
    def test_list_of_square(self, mock_open):
        Base.save_to_file([Square(10, 7, 2, 8), Square(2, 4)])

        dict_01 = '{"id": 8, "size": 10, "x": 7, "y": 2}'
        dict_02 = '{"id": 1, "size": 2, "x": 4, "y": 0}'
        expected = f"[{dict_01}, {dict_02}]"

        mock_open.assert_called_once_with("Square.json", "w", encoding="utf-8")
        mock_open().__enter__().write.assert_called_once_with(expected)


if __name__ == "__main__":
    unittest.main()
