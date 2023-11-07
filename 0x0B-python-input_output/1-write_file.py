#!/usr/bin/python3
"""Defines a module called 1-write_file"""


def write_file(filename="", text=""):
    """Defines a function called write_file."""

    with open(filename, "w", encoding="UTF8") as my_file:
        return my_file.write(text)
