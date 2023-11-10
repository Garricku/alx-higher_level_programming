#!/usr/bin/python3
"""Defines the base module."""


class Base:
    """Defines the class Base."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Defines a class constuctor."""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
