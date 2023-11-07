#!/usr/bin/python3
"""Defines a module called 10-student."""


class Student:
    """Defines a class called Student."""

    def __init__(self, first_name, last_name, age):
        """Defines a constructor for instantiation."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Defines a function to_json that gets a dictionary of a Student."""

        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    new_dict[key] = value
            return new_dict
