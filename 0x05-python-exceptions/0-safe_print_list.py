#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for idx in my_list:
        try:
            if count < x:
                print(idx, end='')
                count += 1

        except Exception:
            pass
    print('')
    return count
