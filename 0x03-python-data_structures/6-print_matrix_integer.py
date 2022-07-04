#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            print("{}".format(j), end=" " if j != i[-1] else "")
        print()

print_matrix_integer([[5,4,3],[2,1,7]]
