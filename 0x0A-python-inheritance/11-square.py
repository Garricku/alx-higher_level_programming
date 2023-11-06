#!/usr/bin/python3
"""Defines the module 11-square."""


Rectangle = __import__("9-rectangle").Rectangle
"""Defines the module Rectangle."""


class Square(Rectangle):
    """Defines a class square that inherits Rectangle."""

    def __init__(self, size):
        """The constructor."""

        super().__init__(size, size)
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """ The magic function is defined here."""

        return "[Square] {}/{}".format(self.__size, self.__size)
