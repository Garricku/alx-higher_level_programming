#!/usr/bin/python3
"""Module for the add_attribute class."""


def add_attribute(obj, name, value):
    """adds an attribute to an object if possible."""

    if hasattr(obj, '__dict__'):
        obj.__dict__[name] = value
    else:
        raise TypeError("can't add new attribute")
