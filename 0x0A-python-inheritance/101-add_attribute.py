#!/usr/bin/python3
def add_attribute(classs, name, value):
    try:
        setattr(classs, name, value)
    except Exception:
        raise TypeError("can't add new attribute")
