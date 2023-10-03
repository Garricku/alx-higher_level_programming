#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i < j:
            if (i + j) > 1:
                print(", ", end='')
            print("{}{}".format(str(i), str(j)), end="")
print('', end='\n')
