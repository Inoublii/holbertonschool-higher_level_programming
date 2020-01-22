#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        x = {}
        for z in attrs:
            try:
                x[z] = self.__dict__[z]
            except Exception:
                continue
        return x
