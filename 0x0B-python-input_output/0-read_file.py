#!/usr/bin/python3
"""Defines a module called 0-read_file."""


def read_file(filename=""):
    """Defines a function called read_file."""

    with open(filename, encoding="UTF8") as my_file:
        print(my_file.read(), end='')
