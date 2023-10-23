#!usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        if b != 0:
            result = a/b
            print("Inside result: {:d}".format(result))
    except ZeroDivisionError:
        raise ZeroDivisionError
    finally:
        print("Inside result: {}".format(result))
        return result
