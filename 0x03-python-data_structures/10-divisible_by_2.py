#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    is_it = []
    for i in my_list:
        if i % 2 == 0:
            is_it.append(True)
        else:
            is_it.append(False)
    return is_it
