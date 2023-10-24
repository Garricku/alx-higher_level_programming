#!/usr/bin/python3
class Square:
    """
    This defines a class called Square.

    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size=0):
        """
        The constructor for the Square class.

        Args:
            size (int): The size of the Square class.

        Raises:
            TypeError: If size is not and interger.
            ValueError: If size is < 0.
        """
        self.__size = size

    @property
    def size(self):
        """
        Retrieves the __size attribute.

        Returns:
            int: The value of the __size attribute.
        """
        return self.__size
    @size.setter
    def size(self, value):
        """
        To set the value of tge __ size attribute.

        Args:
        value (int): The value to be set to the __size atrribute.

        Raises:
            TypeError: If the value is not an interger.
            ValueError: If the value is < 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an interger")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        The method that returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        This method prints a square with '#' charaters.

        If size is equal to 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("#" * self.__size)
