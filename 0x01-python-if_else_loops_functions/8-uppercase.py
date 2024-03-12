#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) in range(97, 123):
            j = ord(i) - 32
            print("{}".format(chr(j)), end="")
    print()
