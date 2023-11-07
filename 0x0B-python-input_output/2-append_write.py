#!/usr/bin/python3
"""Define a module called 2-append_write."""


def append_write(filename="", text=""):
    """Defines a function called append_write."""

    with open(filename, "a", encoding="UTF8") as my_file:
        return my_file.write(text)
