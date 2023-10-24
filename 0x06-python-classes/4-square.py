#!/usr/bin/python3
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
        self.size = size
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
            ValueError: If value is less than o.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        This method returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

