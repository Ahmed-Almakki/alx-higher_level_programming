#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    t1 = list(tuple_a)
    t2 = list(tuple_b)
    t3 = []
    if len(t1) < 2:
        if len(t1) == 0:
            t1 = [0, 0]
        if len(t1) == 1:
            t1 = [t1[0], 0]
    if len(t2) < 2:
        if len(t2) == 0:
            t2 = [0, 0]
        if len(t2) == 1:
            t2 = [t2[0], 0]
    for i in range(2):
        t3.append(t1[i] + t2[i])
    return tuple(t3)
