#!/usr/bin/python3
"""Defines the function that prints a name"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>"

    Args:
        first_name (str): The first name to be printed.
        last_name (str): The last name to be printed. Defaults to an empty string.

    Raises:
        TypeError: If first_name or last_name is not a string.

    Returns:
        None
    """
    # Check that first_name and last_name are strings
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the message
    print("My name is {} {}".format(first_name, last_name))
