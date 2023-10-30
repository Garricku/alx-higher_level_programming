#!/usr/bin/python3
"""Defines the function print_square."""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        TypeError: If size is a float and is less than 0.

    Returns:
        None
    """
    # Check that size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check that size is greater than or equal to 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Check that size is not a float and less than 0
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    # Print the square
    for i in range(size):
        print("#" * size)
