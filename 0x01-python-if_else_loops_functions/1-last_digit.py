#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = str(number)[-1]
last_digit = int(last_digit)
if ((str(number)[0]) == '-') is True:
    last_digit = int(-last_digit)
if last_digit > 5:
    status = " and is greater than 5"
elif last_digit < 6 and last_digit != 0:
    status = " and is less than 6 and not 0"
else:
    status = " and is 0"
print(f"Last digit of {number} is " + str(last_digit) + status)
