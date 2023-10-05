#!/usr/bin/python3
from calculator_1 import add
from calculator_1 import sub
from calculator_1 import mul
from calculator_1 import div
if __name__ == "__main__":
    a = 5
    b = 10
    print(f"{b:d} + {a:d} = {add(b, a):d}")
    print(f"{b:d} - {a:d} = {sub(b, a):d}")
    print(f"{b:d} * {a:d} = {mul(b, a):d}")
    print(f"{b:d} / {a:d} = {div(b, a):d}")
