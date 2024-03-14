#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = number % 10
if x > 5 and number > 0:
    print("Last digit of {} is {} and is greater than 5".format(number, x))
if x < 6 and x != 0 or number < 0:
    if number > 0:
        print("Last digit of {} ".formt(number), end="")
        print("is {} and is less than 6 and not 0".format(x))
    if number < 0:
        n = abs(number) % 10
        print("Last digit of {}".format(number), end="")
        print(" is -{} and is less than 6 and not 0".format(n))
if x == 0:
    print("Last digit of {} is {} and is 0".format(number, x))
