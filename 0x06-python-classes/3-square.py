#!/usr/bin/python3
"""This is for a class defined as Square"""


class Square:
    """
    This class defines a square.

    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size=0):
        """
        The constructor for the Square class.

        Args:
            size (int): The size of the square.

        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        This method returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
