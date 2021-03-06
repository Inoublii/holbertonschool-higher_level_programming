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

    @property
    def size(self):
        return(self.__size)

    @size.setter
    def size(self, value):
        self.__size = value
        if not type(value) == int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        if self.size == 0:
            print()
            return

        for i in range(self.size):
            for x in range(self.size):
                print('#', end='')
            print()
