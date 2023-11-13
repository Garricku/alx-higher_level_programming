#!/usr/bin/python3
"""Defines a unittest."""


import unittest
from models.rectangle import Rectangle
"""Defines the imported modules."""


class TestRectangle(unittest.TestCase):
    """Defines the subclass for testing."""

    def setUp(self):
        """Defines the setUp for test."""
        pass

    def tearDown(self):
        """Defines the tearDown for clean up."""
        pass

    def test_Rectangle(self):
        """Defines the test for rectangle class method."""

        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        r4 = Rectangle(10, 2)
        r4.x = 0

        self.assertRaises(TypeError, Rectangle, 10, "2")
        self.assertRaises(ValueError, Rectangle, -10, 2)
        self.assertRaises(TypeError, setattr, r4, 'x', {})
        self.assertRaises(ValueError, Rectangle, 10, 2, 3, -1)

    def test_area(self):
        """Test the method area."""

        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)

        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        """Test the method display."""

        r1 = Rectangle(4, 6)
        r1_expected_output = "####\n####\n####\n####\n####\n####\n"
        self.assertEqual(r1.display(), r1_expected_output)

        r2 = Rectangle(2, 2)
        r2_expected_output = "##\n##\n"
        self.assertEqual(r2.display(), r2_expected_output)

        r3 = Rectangle(2, 3, 2, 2)
        r3_expected_output = "  ##\n  ##\n  ##\n"
        self.assertEqual(r1.display(), r1_expected_output)

        r4 = Rectangle(3, 2, 1, 0)
        r4_expected_output = " ###\n ###\n"
        self.assertEqual(r2.display(), r2_expected_output)

    def test_str(self):
        """Test the method str."""

        r1 = Rectangle(4, 6, 2, 1, 12)
        r1_expected_output = "[Rectangle] (12) 2/1 - 4/6\n"
        self.assertEqual(str(r1), r1_expected_output)

        r2 = Rectangle(5, 5, 1)
        r2_expected_output = "[Rectangle] (1) 1/0 - 5/5\n"
        self.assertEqual(str(r2), r2_expected_output)

    def test_update(self):
        """Test the method update."""

        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")

        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")

        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")

        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")

        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/1")

        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (1) 2/10 - 1/1")

        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/1")

        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")


    def test_to_dictionary(self):
        """Test the method to_dictionary."""

        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(r1.to_dictionary(), r1_dictionary)

        r2 = Rectangle(1, 1)
        r2_dictionary = {'id': 2, 'width': 1, 'height': 1, 'x': 0, 'y': 0}
        self.assertEqual(r2.to_dictionary(), r2_dictionary)


if __name__ == '__main__':
    unittest.main()
