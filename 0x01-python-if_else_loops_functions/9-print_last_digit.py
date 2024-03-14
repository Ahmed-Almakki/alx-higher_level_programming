#!/usr/bin/python3
def print_last_digit(number):
    n = abs(number)
    x = n % 10
    print("{}".format(x), end="")
    return n % 10
