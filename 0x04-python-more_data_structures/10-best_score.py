#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    bigK = list(a_dictionary.keys())[0]
    bigV = a_dictionary[bigK]

    for i, j in a_dictionary.items():
        if j > bigV:
            bigK = i
            bigV = j
    return bigK
