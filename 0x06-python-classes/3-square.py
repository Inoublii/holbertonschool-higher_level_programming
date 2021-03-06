#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.__size = size
        if not type(size) == int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):

        return(self.__size * self.__size)
__doc__ = " Square class"
