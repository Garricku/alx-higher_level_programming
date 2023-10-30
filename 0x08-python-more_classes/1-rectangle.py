#!/usr/bin/python3
"""This is a method that defines a rectangle."""


class Rectangle:
    """
    A classs that defines a rectangle.

    Attributes:
        __width: The width of the rectangle.
        __height: The hieght of the rectangle.

    Raises:
        TypeError: If width or height is not an integer.
        ValueError: If width or height is less that 0.

    Returns: The Rectangle.
    """

    def __init__(self, width=0, height=0):
        """Initializes a new instance of Rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the value of height of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Returns the value of height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    if __name__ == '__main__':
        pass
