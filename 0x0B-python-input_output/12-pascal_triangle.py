#!/usr/bin/python3
"""Defines a module called 12-pascal_triangle."""


def pascal_triangle(n):
    """Defines a function that returns a list of lists of integers."""

    my_list = []
    if n <= 0:
        return my_list

    my_list = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(my_list[i - 1][j - 1] + my_list[i - 1][j])
        row.append(1)
        my_list.append(row)
    return my_list
