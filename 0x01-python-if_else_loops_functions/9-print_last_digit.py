#!/usr/bin/python3
def print_last_digit(number):
    last_digit = str(number)[-1]
    if (ord(last_digit)) >= ord('0') and (ord(last_digit)) <= ord('9'):
        print(last_digit, end='')
        return last_digit
    else:
        raise ValueError("Invalid input")
