#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """ prints number of lines
        Args:
            filename
            nb_lines: number of lines
    """
i = 0
with open(filename, encoding='utf-8') as x:
    if nb_lines <= 0:
        print(f.read(), end='')
    else:
        for line in f:
            i += 1
            if i == nb_lines:
                break
            print(line, end='')
