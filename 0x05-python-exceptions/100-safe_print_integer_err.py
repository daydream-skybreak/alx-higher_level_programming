#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as vr:
        sys.stderr.write("Exception: {}".format(vr))
        return False
