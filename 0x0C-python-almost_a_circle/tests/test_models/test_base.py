#!/usr/bin/python3
"""Defines a unittest."""


import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
"""Imports the unittest module and the Base class/method."""


class TestBase(unittest.TestCase):
    """Defines the subclass of the unittest.TestCase."""

    def setUp(self):
        """Testing with an integer argument value."""
        pass

    def tearDown(self):
        """Defines the tearDown method for clean up."""
        del self.id

    def test_id(self):
        """Defines the test method for id."""

        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base(4)
        self.assertEqual(b5.id, 4)

    def test_to_json_string(self):
        """Defines the test for the method."""

        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json.loads(json_dictionary), [dictionary])

    def test_from_json_string(self):
        """Defines the test for the method."""

        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, list_input)

    def test_create(self):
        """Defines the test for the method."""

        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_save_to_file_csv(self):
        """Defines the test for the method."""

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file_csv(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file_csv()

        for rect in list_rectangles_input:
            self.assertTrue(rect in list_rectangles_output)

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]

        Square.save_to_file_csv(list_squares_input)

        list_squares_output = Square.load_from_file_csv()

        for square in list_squares_input:
            self.assertTrue(square in list_squares_output)


if __name__ == "__main___":
    unittest.main()
