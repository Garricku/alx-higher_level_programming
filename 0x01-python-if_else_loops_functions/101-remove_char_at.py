#!/usr/bin/python3
def remove_char_at(str, n):
    for i in str:
        if i == n:
            continue
        else:
            copy += chr(i)
    return copy
