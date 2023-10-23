#!/usr/bun/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > len([a, b]):
                raise Exception("Too far")
            else:
                result += ([a, b][i-1] ** i) / (i)
        except Exception:
            result += a + b
            break
    return result
