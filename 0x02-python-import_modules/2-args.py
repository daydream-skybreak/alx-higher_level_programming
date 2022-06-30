#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    b = len(sys.argv) - 1
    if b == 0:
        print("{} arguments.".format(b))
    elif b == 1:
        print("{} argument:\n{}: {}".format(b, 1, sys.argv[1]))
    else:
        print("{} arguments:".format(b))
        for i in range(1, b + 1):
            print("{}: {}".format(i, sys.argv[i]))
