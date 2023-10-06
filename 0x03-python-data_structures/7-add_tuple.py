#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = (0, 0)
    if len(tuple_a) >= 1:
        new_tuple = (new_tuple[0] + tuple_a[0], new_tuple[1])
    if len(tuple_a) == 2:
        new_tuple = (new_tuple[0], new_tuple[1] + tuple_a[1])
    if len(tuple_b) >= 1:
        new_tuple = (new_tuple[0] + tuple_b[0], new_tuple[1])
    if len(tuple_b) == 2:
        new_tuple = (new_tuple[0], new_tuple[1] + tuple_b[1])
    return new_tuple
