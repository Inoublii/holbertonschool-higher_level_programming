#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Define: Rectangle class"""


class Rectangle(BaseGeometry):
    """
    class Rectangle(BaseGeometry
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width__ = width
        self.__height__ = height

    def area(self):
        """ calculates rectange area
        Return: int
        """
        return (self.__width__ * self.__height__)

    def __str__(self):
        """prints a string that represent the Rectangle
        Return: string
        """
        return("[Rectangle] {:d}/{:d}".format(self.__height__, self.__width__))
