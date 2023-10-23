#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    num = None
    try:
        print("{:d}".format(int(value)))
        num = True
    except TypeError as err:
        print("Exception: ", err, file=sys.stderr)
        num = False
    finally:
        return num
