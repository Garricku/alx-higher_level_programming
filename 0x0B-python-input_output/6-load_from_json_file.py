#!/usr/bin/python3
"""Defines a module called 6-load_from_json_file."""


import json
"""Defines the imported module json."""


def load_from_json_file(filename):
    """Defines a function called load_from_json_file."""

    with open(filename, "r", encoding="UTF8") as my_file:
        return json.load(my_file)
