#!/usr/bin/python3
def number_of_lines(filename=""):
    """ counts lines"""
    line = 0
    with open(filename, encoding='utf-8') as f:
        for x in f:
            line = line + 1
    return line
