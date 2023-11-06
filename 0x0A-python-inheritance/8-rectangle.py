#!/usr/bin/python3
"""The module BaseGeometry"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry
"""Port the module for the class BaseGeometry."""


class Rectangle(BaseGeometry):
    """Defines a class rectangle."""

    def __init__(self, width, height):
        """The constructor."""

        super().__init__()
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
