#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    new = {key: val for val, key in a_dictionary.items()}
    r = max([i for i in new.keys()])
    return new[r]
