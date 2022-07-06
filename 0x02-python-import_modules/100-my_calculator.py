#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(sys.argv[1])
        c = sys.argv[2]
        b = int(sys.argv[3])
        if c == "+":
            result = add(a, b)
            print("{0:d} {1} {2:d} = {3}".format(a, c, b, result))
        elif c == "-":
            result = sub(a, b)
            print("{0:d} {1} {2:d} = {3}".format(a, c, b, result))
        elif c == "*":
            result = mul(a, b)
            print("{0:d} {1} {2:d} = {3}".format(a, c, b, result))
        elif c == "/":
            result = div(a, b)
            print("{0:d} {1} {2:d} = {3}".format(a, c, b, result))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
