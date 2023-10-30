#!/usr/bin/python3
"""
add_integer module for the addition function.
Tested with docstrings.
Test files in test directory.
"""


def add_integer(a, b=98):
    """
    Defines an addition function.

    Args:
        a (int): The number to be added to number b.
        b (int): The number to be added to number a. Default value is 98.

    Raises:
        TypeError: If a or b is not an interger or float.

    Returns:
        The sum of a and b.
    """
    result = 0
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
