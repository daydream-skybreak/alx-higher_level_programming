#!/usr/bin/python3
def search_replace(my_list, search, replace):
    idx = 0
    my_list1 = [replace if i == search else i for i in my_list]
    return my_list1
