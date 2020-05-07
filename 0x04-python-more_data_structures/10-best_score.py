#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best = 0
    for i, j in a_dictionary.items():
        if j > best:
            best = j
    for i, j in a_dictionary.items():
        if j == best:
            return(i)
