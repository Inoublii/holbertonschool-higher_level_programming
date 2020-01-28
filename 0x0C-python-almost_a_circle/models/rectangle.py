#!/usr/bin/python3
'''import rbase'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle Class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        """define Rectangle """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """"rectange str"""
        return("[Rectangle] (%s) %s/%s - %s/%s" % (self.id, self.x, self.y,
                                                   self.width, self.height))

    def update(self, *args, **kwargs):
        """updare def"""
        if "id" in kwargs:
            self.id = kwargs["id"]
        elif len(args) > 0:
            self.id = args[0]
        if "width" in kwargs:
            self.__width = kwargs['width']
        elif len(args) > 1:
            self.__width = args[1]
        if "height" in kwargs:
            self.__height = kwargs['height']
        elif len(args) > 2:
            self.__height = args[2]
        if "x" in kwargs:
            self.__x = kwargs["x"]
        elif len(args) > 3:
            self.__x = args[3]
        if 'y' in kwargs:
            self.__y = kwargs['y']
        elif len(args) > 4:
            self.__y = args[4]

    def area(self):
        '''area function'''
        return (self.__width * self.__height)

    def display(self):
        '''display function'''
        for a in range(self.__y):
            print()
        for a in range(self.__height):
            for a in range(self.__x):
                print(end=" ")
            for a in range(self.__width):
                print(end="#")
            print()

    def to_dictionary(self):
            """dictionairy"""
            dic = {
                "x": self.x, "width": self.width, "id": self.id,
                "height": self.height, "y": self.y,
            }
            return (dic)

    @property
    def width(self):
        '''width property'''
        return self.__width

    @property
    def height(self):
        '''height property'''
        return self.__height

    @property
    def x(self):
        '''x property'''
        return self.__x

    @property
    def y(self):
        '''y property'''
        return self.__y

    @height.setter
    def height(self, value):
        '''height Setter'''
        if type(value) is int:
            if value > 0:
                self.__height = value
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @width.setter
    def width(self, value):
        '''width Setter'''
        if type(value) is int:
            if value > 0:
                self.__width = value
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @x.setter
    def x(self, value):
        '''x Setter'''
        if type(value) is int:
            if value >= 0:
                self.__x = value
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    @y.setter
    def y(self, value):
        '''y Setter'''
        if type(value) is int:
            if value >= 0:
                self.__y = value
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")
