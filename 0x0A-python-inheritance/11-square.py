#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define: Square class
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size__ = size
        super().__init__(size, size)

    def area(self):
        """calculate square area"""
        return(self.__size__ ** 2)

    def __str__(self):
        """prints a string that represent the Rectangle
        Return: string
        """
        return("[Square] {:d}/{:d}".format(self.__size__, self.__size__))
