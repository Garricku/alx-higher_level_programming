#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        if fct not None:
            result = fct(*args)
    except Exception as err:
        print("Exception: ", err, file=sys.stderr)
        result = None
    return result
