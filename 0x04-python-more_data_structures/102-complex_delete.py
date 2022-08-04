#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    iterable = a_dictionary.keys()
    keys = []
    for k in iterable:
        if a_dictionary[k] == value:
            keys.append(k)
    for i in keys:
        del a_dictionary[i]
    return a_dictionary
