#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    for j in my_list:
        count += 1
    if (count == 0) or (x == 0) or (x > count):
        return 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
        except IndexError:
            break
    print()
    return i + 1
