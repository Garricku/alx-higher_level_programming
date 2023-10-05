#!/usr/bin/python3
from calculator_1 import add
from calculator_1 import sub
from calculator_1 import mul
from calculator_1 import div
import sys
if __name__ == "__main__":
    if len(sys.argv) == 4:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        operator = sys.argv[2]
        if operator == '+':
            print(f"{a:d} {operator} {b:d} = {add(a, b):d}")
        elif operator == '-':
            print(f"{a:d} {operator} {b:d} = {sub(a, b):d}")
        elif operator == '*':
            print(f"{a:d} {operator} {b:d} = {mul(a, b):d}")
        elif operator == '/':
            print(f"{a:d} {operator} {b:d} = {div(a, b):d}")
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
