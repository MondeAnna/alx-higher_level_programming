#!/usr/bin/python3
"""
Unittest for max_integer
"""

from unittest import TestCase
from unittest import main


max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(TestCase):
    """
    test suite for max
    """

    def test_empy_list(self):
        result_no_arg = max_integer()
        self.assertIsNone(result_no_arg)

        result_empty_list = max_integer([])
        self.assertIsNone(result_empty_list)

    def test_negative_nums(self):
        result = max_integer([-5, -1])
        self.assertEqual(result, -1)

    def test_positive_nums(self):
        result = max_integer([5, 1])
        self.assertEqual(result, 5)


if __name__ == "__main__":
    main()
