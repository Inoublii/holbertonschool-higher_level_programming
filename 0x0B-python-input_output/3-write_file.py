#!/usr/bin/python3
def write_file(filename="", text=""):
    """ writes text into file and return len(text)"""
    with open(filename, 'x', encoding='utf-8') as x:
        return(x.write(text))
