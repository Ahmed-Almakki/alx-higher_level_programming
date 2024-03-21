#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new = [(ky, val) for val, ky in a_dictionary.items()]
    r = []
    for i in new:
        if i[0] != value:
            r.append(i)
    a_dictionary.clear()
    for i in r:
        a_dictionary[i[1]] = i[0]
    return a_dictionary
