#!/usr/bin/python3
"""This is a module"""


class BaseGeometry:
    """Defines a class BaseGeometry."""

    def area(self):
        """Defines an area function (not implemented yet)."""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validadtes the value variable."""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
