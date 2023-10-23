#!usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        if b != 0:
            result = a/b
    except ZeroDivisionError:
        raise ZeroDivisionError
    else:
        print("Inside result: {}".format(result))
    finally:
        return result
