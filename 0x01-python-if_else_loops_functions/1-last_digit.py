#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = str(number)[-1]
last_digit = int(last_digit)
a = 5
b = 6
c = 0
if ((str(number)[0]) == '-') is True:
    last_digit = int(-last_digit)
if last_digit > 5:
    status = " and is greater than {:d}".format(a)
elif last_digit < 6 and last_digit != 0:
    status = " and is less than {:d} and not {:d}".format(b, c)
else:
    status = " and is {:d}".format(c)
print(f"Last digit of {number:d} is {last_digit:d}{status}")
