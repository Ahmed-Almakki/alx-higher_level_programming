#!/usr/bin/python3
def no_c(my_string):
    s, lst = "", []
    for i in list(my_string):
        if ord(i) != 99 and ord(i) != 67:
            lst.append(i)
    return s.join(lst)
