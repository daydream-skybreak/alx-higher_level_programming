#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    lis = []
    for i in my_list:
        if i not in lis:
            result += i
            lis.append(i)
    return result
