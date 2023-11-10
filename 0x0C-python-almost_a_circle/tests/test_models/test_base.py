#!/usr/bin/python3
"""Defines a unittest."""


import unittest
from models.base import Base
"""Imports the unittest module and the Base class/method."""


class TestBase(unittest.TestCase):
    """Defines the subclass of the unittest.TestCase."""

    def setUp(self):
        """Testing with an integer argument value."""

        self.id = Base(3)

    def tearDown(self):
        del self.id


if __name__ == "__main___":
    unittest.main()
