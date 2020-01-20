#!/usr/bin/python3
"""
2-matrix_divided"
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix
    """
    x = None
    if type(matrix) != list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for l in matrix:
        if type(l) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if x is None:
            x = len(l)
        elif x != len(l):
            raise TypeError("Each row of the matrix must have the same size")
        for i in l:
            if type(i) != int and type(i) != float:
                raise TypeError(
                 "matrix must be a matrix (list of lists) of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    return [[round(i / div, 2) for i in l] for l in matrix]
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
