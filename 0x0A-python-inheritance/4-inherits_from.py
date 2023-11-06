#!/usr/bin/python3
"""Module for inherits func"""


def inherits_from(obj, a_class):
    return isinstance(obj, a_class) and type(obj) != a_class
