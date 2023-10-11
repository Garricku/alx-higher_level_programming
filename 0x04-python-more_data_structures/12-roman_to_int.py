#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) and roman_string is not None:
        num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(roman_string)):
            value = num.get(roman_string[i], 0)
            lenth = (len(roman_string) - 1)
            if i < lenth and num.get(roman_string[i + 1], 0) > value:
                result -= value
            else:
                result += value
        return result

    else:
        return 0
