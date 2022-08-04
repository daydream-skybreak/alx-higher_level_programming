#!/usr/bin/python3


def weight_average(my_list=[]):
    total, denom = (0, 0)

    if len(my_list) == 0:
        return 0

    for i in range(len(my_list)):
        val, weight = my_list[i]
        total += (val * weight)
        denom += weight

    return total / denom
