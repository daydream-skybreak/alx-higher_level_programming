#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 65 and ord(i) <= 90:
            print("{0}".format(chr(ord(i)+32)), end = "")
        else:
            print("{0}".format(i, end = "")
    print('\n')
