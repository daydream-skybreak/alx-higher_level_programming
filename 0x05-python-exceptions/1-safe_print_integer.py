#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False

nb = safe_print_integer(57.43)
nc = safe_print_integer("School")
if not nb:
    print("not printed")
if not nc:
    print("not printed")