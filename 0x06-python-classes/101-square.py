#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    This class defines a square.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        The constructor for the Square class.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.

        Raises:
            TypeError: If size is not an integer or if position is not a tuple
            of 2 positive integers.
            ValueError: If size is less than 0 or if position contains
            negative integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        This method retrieves the value of the __size attribute.

        Returns:
            int: The value of the __size attribute.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This method sets the value of the __size attribute.

        Args:
            value (int): The value to set the __size attribute to.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        This method retrieves the value of the __position attribute.

        Returns:
            tuple: The value of the __position attribute.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        This method sets the value of the __position attribute.

        Args:
            value (tuple): The value to set the __position attribute to.

        Raises:
            TypeError: If value is not a tuple or if it does not contain 2
            integers.
            ValueError: If either integer in the tuple is less than 0.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) for i in value) or \
                not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        This method returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints a square with '#' characters using position information.

        If size is equal to 0, it prints an empty line. Position should be used
        by using space - Don’t fill lines by spaces when position[1] > 0.
        """
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Returns a string representation of this Square instance.
        """
        result = ""

        for i in range(self.__position[1]):
            result += "\n"

        for i in range(self.__size):
            result += " " * self.__position[0] + "#" * self.__size + "\n"

        return result[:-1]
