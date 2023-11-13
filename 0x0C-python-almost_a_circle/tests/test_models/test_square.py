#!/usr/bin/python3
"""Defines a unittest module for Square."""

import unittest
from models.square import Square
"""Defines the imported modules."""


class TestSquare(unittest.TestCase):
    """Defines the test suite for the class methods."""

    def test_display(self):
        """Defines the test of the method for display."""

        s1 = Square(5)
        s1_expected_output = "#####\n#####\n#####\n#####\n#####\n"
        self.assertEqual(s1.display(), s1_expected_output)

        s2 = Square(2, 2)
        s2_expected_output = "  ##\n  ##\n"
        self.assertEqual(s2.display(), s2_expected_output)

        s3 = Square(3, 1, 3)
        s3_expected_output = "\n\n\n ###\n ###\n ###\n"
        self.assertEqual(s3.display(), s3_expected_output)

    def test_size(self):
        """Defines the test for the method size."""

        s1 = Square(5)
        self.assertEqual(s1.size, 5)

        s1.size = 10
        self.assertEqual(s1.size, 10)

        with self.assertRaises(TypeError):
            s1.size = "9"

        with self.assertRaises(ValueError):
            s1.size = -1

    def test_update(self):
        """Defines the test for the method update."""

        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")

        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")

        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")

        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")

        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")

        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] (1) 12/4 - 2")

        s1.update(size=7, y=1)
        self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")

        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")

    def test_to_dictionary(self):
        """Defines the test for the method to_dictionary."""

        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)

        self.assertEqual(str(s1), str(s2))
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)


if __name__ == '__main__':
    unittest.main()
