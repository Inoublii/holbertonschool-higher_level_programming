#!/usr/bin/python3
def lookup(obj):
    """
    function that returns the list of available attributes
    and methods of an object
    args:
    obj: objet
    RETURN: list
    """
    return dir(obj)
