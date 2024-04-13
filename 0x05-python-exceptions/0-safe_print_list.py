#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    if x == 0:
        return 0
    for j in my_list:
        count += 1
    try:
        for i in range(x):
            print(my_list[i], end="")
        print()
    except IndexError:
        pass
    return i + 1
