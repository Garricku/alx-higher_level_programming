#!/usr/bin/python3
"""A class Square that defines a square"""


class Square:
    """
    This class defines a square.

    Attributes:
        __size (float): The size of the square.
    """
    def __init__(self, size=0):
        """
        The constructor for the Square class.

        Args:
            size (float): The size of the square.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        This method retrieves the value of the __size attribute.

        Returns:
            float: The value of the __size attribute.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This method sets the value of the __size attribute.

        Args:
            value (float): The value to set the __size attribute to.

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = float(value)

    def area(self):
        """
        This method returns the area of the square.

        Returns:
            float: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Determines if this Square instance is equal to another Square instance.

        Args:
            other (Square): The other Square instance to compare to.

        Returns:
            bool: True if this Square instance is equal to other, else False.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Determines if this Square instance is not equal to another Square obj.

        Args:
            other (Square): The other Square instance to compare to.

        Returns:
            bool: True if this Square instance is not equal to other,
            False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Determines if this Square instance is greater than another Square instance.

        Args:
            other (Square): The other Square instance to compare to.

        Returns:
            bool: True if this Square instance is greater than other,
            False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Determines if this Square instance is greater than or equal to 
        another Square instance.

        Args:
            other (Square): The other Square instance to compare to.

        Returns:
            bool: True if this Square instance is greater than or equal to other,
            False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Determines if this Square instance is less than another Square instance.

        Args:
            other (Square): The other Square instance to compare to.

        Returns:
            bool: True if this Square instance is less than other,
            False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Determines if this Square instance is less than or equal to another
        Square instance.

        Args:
            other (Square): The other Square instance to compare to.

        Returns:
            bool: True if this Square instance is less than or equal to other,
            False otherwise.
        """
        return self.area() <= other.area()

