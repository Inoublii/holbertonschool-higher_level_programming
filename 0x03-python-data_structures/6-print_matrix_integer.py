#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for s in range(0, len(x)):
            print(end="{:d}".format(x[s]))
            if s != len(x) - 1 :
                print(end=" ")
        print("")
