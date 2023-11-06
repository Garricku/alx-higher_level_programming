#!/usr/bin/python3
"""This is for the Rectangle module."""


BaseGeometry = __import__("7-base_geometry").BaseGeometry
"""Imports the module BaseGeometry"""


class Rectangle(BaseGeometry):
    """Defines a class Rectangle"""

    def __init__(self, width, height):
        """The constructor."""

        super().__init__()
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Defines an area function"""

        return self.__width * self.__height

    def __str__(self):
        """Defines a magic function."""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
