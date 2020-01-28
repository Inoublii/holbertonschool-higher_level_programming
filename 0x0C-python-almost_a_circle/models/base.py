#!/usr/bin/python3
import json
"""define Base class"""


class Base:
    """represent Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """define __init__"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """dictionairy to Json"""
        if list_dictionaries is None:
            list_dictionaries = []
        return (json.dumps(list_dictionaries))
