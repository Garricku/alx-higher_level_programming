#!/usr/bin/python3
"""Defines a module 10-square.py."""


Rectangle = __import__("9-rectangle").Rectangle
"""The module Rectangle."""


class Square(Rectangle):
    """Defines a class Square that inherits rectangle."""

    def __init__(self, size):
        """The constuctor."""

        super().__init__(size, size)
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """Defines a magic function"""

        return "[Square] {}/{}".format(self.__size, self.__size)
