#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    ln = len(my_list)
    if len(my_list) == 0:
        print("[]")
    else:
        for i in range(ln - 1, -1, -1):
            print("{:d}".format(my_list[i]))
