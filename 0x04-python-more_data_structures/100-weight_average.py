#!/usr/bin/python3
def weight_average(my_list=[]):
    sm, den = 0, 0
    if len(my_list) == 0:
        return 0
    for i in my_list:
        sm += i[0] * i[1]
        den += i[1]
    return sm / den
