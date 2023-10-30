#!/usr/bin/python3
"""
A function that divides all elements of a matrix.
Tests the function for functionality.
Check for errror messages.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int or float): The number to divide the elements of the matrix by.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats, or
        if div is not an integer or float.
        valueError: If each row of the matrix does not have the same size.
        ZeroDivisionError: If div is equal to 0.

    Returns:
        A new matrix with all elements divided by div, rounded to 2 decimal
        places.
    """
    if isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(row, list) \
            and all(isinstance(x, (int, float)) for x in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(dic, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(x/div, 2) for x in row] for row in matrix]
