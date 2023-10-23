#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    num = [int, float]
    try:
        for i in range(list_length):
            if type(my_list_1[i]) not in num or type(my_list_2[i]) not in num:
                result.append(0)
                raise TypeError("wrong type")
            if my_list_2[i] == 0:
                result.append(0)
                raise ZeroDivisionError("division by 0")
            if my_list_1[i] is None or my_list_2[i] is None:
                result.append(0)
                raise IndexError("out of range")
            else:
                result.append(my_list_1[i]/my_list_2[i])
    except TypeError as err1:
        print(err1)
    except ZeroDivisionError as err2:
        print(err2)
    except IndexError as err3:
        print(err3)
    finally:
        return result
