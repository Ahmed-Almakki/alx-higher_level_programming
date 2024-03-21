#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    i = 0
    lst_k = [i for i in sorted(a_dictionary.keys())]
    lst_val = [a_dictionary[i] for i in lst_k]
    for j in lst_k:
        if j == key:
            lst_k.pop(i)
            lst_val.pop(i)
        i += 1
    a_dictionary.clear()
    for i in range(len(lst_k)):
        a_dictionary[lst_k[i]] = lst_val[i]
    return a_dictionary
