#!/usr/bin/python3
"""Defines a module 100-append_after."""


def append_after(filename="", search_string="", new_string=""):
    """Defines a function that insert a line of text after a string."""

    with open(filename, "r") as my_file:
        lines = my_file.readlines()

    with open(filename, "w") as my_file:
        for line in lines:
            my_file.write(line)
            if search_string in line:
                my_file.write(new_string + '\n')
