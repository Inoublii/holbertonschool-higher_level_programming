#!/usr/bin/python3
"""
Define: Strudent Class
"""


class Student:
    """Represents a Rectangle
    """
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

    def reload_from_json(self, json):
        for a in json:
            try:
                setattr(self, a, json[a])
            except Exception:
                continue
