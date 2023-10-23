#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        is_num = True
    except Exception:
        is_num = False
    return is_num
