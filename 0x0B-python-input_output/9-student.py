#!/usr/bin/python3
"""Defines a module called 9-student."""


class Student:
    """Defines a class called Student."""

    def __init__(self, first_name, last_name, age):
        """The constructor for instantiation."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Defines a function that retrieves a dictionary of a Student."""

        return self.__dict__
