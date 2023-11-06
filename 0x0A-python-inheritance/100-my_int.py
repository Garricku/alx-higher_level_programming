#!/usr/bin/python3
"""Module for Myint"""


class MyInt(int):
    """Defines a class MyInt."""

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
