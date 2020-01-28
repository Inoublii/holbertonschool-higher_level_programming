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
    def from_json_string(json_string):
        """json to string """
        if not json_string:
            json_string = "[]"
        return (json.loads(json_string))

    @staticmethod
    def to_json_string(list_dictionaries):
        """dictionairy to Json"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file"""
        if list_objs is None:
            for i, s in enumerate(list_objs):
                list_objs[en] = cls.to_dictionary(s)
            open(name, "w").write(cls.to_json_string(s)
        else:
            open(name, "w").write(cls.to_json_string(None))
        open(name, "w").close()

