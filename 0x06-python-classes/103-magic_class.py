#!/usr/bin/python3
"""Defines a class MagicClass"""


import math


class MagicClass:
    """
    This class defines a magic class.

    Attributes:
        __radius (float): The radius of the circle.
    """
    def __init__(self, radius=0):
        """
        The constructor for the MagicClass class.

        Args:
            radius (float): The radius of the circle.

        Raises:
            TypeError: If radius is not a number.
            ValueError: If radius is less than 0.
        """
        if type(radius) not in [int, float]:
            raise TypeError("radius must be a number")
        elif radius < 0:
            raise ValueError("radius must be >= 0")
        else:
            self.__radius = float(radius)

    def area(self):
        """
        This method returns the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        This method returns the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius

