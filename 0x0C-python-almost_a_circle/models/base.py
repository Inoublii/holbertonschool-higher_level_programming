#!/usr/bin/python3
"""define Base class"""
import json


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
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """json to string """
        if not json_string:
            json_string = "[]"
        return (json.loads(json_string))

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file"""
        filename = cls.__name__ + ".json"
        openn = open(filename, "w")
        if list_objs is not None:
            for i, s in enumerate(list_objs):
                list_objs[i] = cls.to_dictionary(s)
            openn.write(cls.to_json_string(list_objs))
        else:
            openn.write(cls.to_json_string(None))
        openn.close()
