#!/usr/bin/python3
""" a function to divide a list by a given number """


def matrix_divided(matrix, div):
    size = None  
    for i in range(len(matrix)):
        if type(matrix[i]) != list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for j in matrix[i]:
            if type(j) not in [int, float]:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")

        if size == None:
            size = len(matrix[i])

        if len(matrix[i]) != size and i != 0:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []

    for row in matrix:
        new_matrix.append(list(map(lambda x: round(x / div, 2), row)))

    return new_matrix
