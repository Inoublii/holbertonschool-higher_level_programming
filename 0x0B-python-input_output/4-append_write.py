#!/usr/bin/python3
def append_write(filename="", text=""):
    """ append to File
    """
    with open(filename, 'x', encoding='utf-8') as x:
        return(x.write(text))
