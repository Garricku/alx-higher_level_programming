#!/usr/bin/python3
def uppercase(str):
    upper = ''
    for i in str:
        if i >= 'a' and i <= 'z':
            upper += chr((ord(i) - 32))
        else:
            upper += i
    print(upper)
