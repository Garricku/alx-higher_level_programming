#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_mul_of_2 = []
    for mul_of_2 in my_list:
        if mul_of_2 % 2 == 0:
            list_mul_of_2.append(True)
        else:
            list_mul_of_2.append(False)
    return list_mul_of_2
