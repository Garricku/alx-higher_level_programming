#!/usr/bin/python3
"""Defines the module called 5-save_to_json_file."""


import json
"""Defines the imported module json."""


def save_to_json_file(my_obj, filename):
    """Defines the function called save_to_json_file."""

    with open(filename, "w", encoding="UTF8") as my_file:
        json.dump(my_obj, my_file)
