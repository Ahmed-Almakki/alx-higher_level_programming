#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for ky in sorted(a_dictionary.keys()):
        print(ky + ":", a_dictionary[ky])
