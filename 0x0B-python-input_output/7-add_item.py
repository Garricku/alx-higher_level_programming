#!/usr/bin/python3
"""Defines a module called 7-add_item."""

import sys
"""Imports the sys module."""

import os.path
"""Imports the os path modele."""

from os import path
"""Imports the path os module."""

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
"""Defines the functions imported from 5-save_to_json_file module."""


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""Defines the functions imported from 6-load_from_json_file module."""


if __name__ == "__main__":
    filename = "add_item.json"
    my_list = []

    if path.exists(filename):
        my_list = load_from_json_file(filename)

    for arg in sys.argv[1:]:
        my_list.append(arg)

    save_to_json_file(my_list, "add_item.json")
