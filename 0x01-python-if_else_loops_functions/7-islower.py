#!/usr/bin/python3
def islower(c):
    for i in range(ord('a'), ord('z') + 1):
        if c == chr(i):
            return True
    if c < ord('a') or c > ord('z') and c < ord('A') or c > ord('Z'):
        raise ValueError("Invalid input")
    else:
        return False
