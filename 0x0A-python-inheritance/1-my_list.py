#!/usr/bin/python3
"""This module is for the lists class."""


class MyList(list):
    """Defines a class called MyList that inherits from list."""

    def print_sorted(self):
        """Prints sorted information of the class Mylist."""

        print(sorted(self))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
