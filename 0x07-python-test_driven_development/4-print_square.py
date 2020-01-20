#!/usr/bin/python3
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
"""print_square"""


def print_square(size):
    """printing a square with #s
    int:
    size: size of the square
    Raises:
        TypeError: If size is not int
        ValueError: If size < 0
    """
    if type(size) is not int and type(size) is not float:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(int(size)):
        for z in range(int(size)):
            print("#", end="")
        print()
