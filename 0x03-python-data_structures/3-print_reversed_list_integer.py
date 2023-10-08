#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    if len(my_list) == 1:
        return my_list
    reversed_list = reversed(my_list)
    for num in reversed_list:
        print("{:d}".format(num))
