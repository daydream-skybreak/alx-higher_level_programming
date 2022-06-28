#!/usr/bin/python3
beg = 96
for i in range(26):
    beg += 1
    if beg == 101 or beg == 113:
        continue
    print("{0}".format(chr(beg)), end="")
