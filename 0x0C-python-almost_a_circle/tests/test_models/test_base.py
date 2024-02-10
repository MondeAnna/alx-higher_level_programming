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


class TestInitialisation(TestBase):

    """ Test Initialisation
    """

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


class TestToJsonString(TestBase):

    """ Test Conversion to JSON String
    """

    def test_converting_none(self):
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_converting_empty_list_of_dictionaries(self):
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_converting_list_of_dictionaries(self):
        list_dict = [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]
        result = Base.to_json_string(list_dict)
        expected = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
