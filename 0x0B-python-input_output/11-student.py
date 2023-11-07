#!/usr/bin/python3
"""defines a module called 11-student."""


class Student:
    def __init__(self, first_name, last_name, age):
        """Defines a constructor."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Defines a function that gets the dictionary representation."""

        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    new_dict[key] = value
            return new_dict

    def reload_from_json(self, json):
        """Defines a function reload_from_json."""

        for key, value in json.items():
            setattr(self, key, value)
