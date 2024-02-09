#!/usr/bin/python


""" Test Base Class
"""


import unittest


from models.base import Base


class TestBase(unittest.TestCase):

    """ Test Base Class
    """

    def setUp(self):
        self.__nb_objects = Base._Base__nb_objects

    def tearDown(self):
        Base._Base__nb_objects = self.__nb_objects

    def test_no_id(self):
        base = Base()
        self.assertEqual(base.id, 1)

    def test_init_with_id(self):
        base = Base(616)
        self.assertEqual(base.id, 616)

    def test_varied_instances_with_and_without_id(self):
        bases = [(1, Base()), (2, Base()), (44, Base(44)), (3, Base())]
        for expected_id, base in bases:
            self.assertEqual(base.id, expected_id)


if __name__ == "__main__":
    unittest.main()
