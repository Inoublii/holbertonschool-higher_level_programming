#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """ prints number of lines
        Args:
            filename
            nb_lines: number of lines
    """
    with open(filename, encoding='utf-8') as x:
        if nb_lines <= 0:
            print(x.read(), end="")
        else:
            i = 0
            for line in x:
                i += 1
                print(line, end='')
                if i == nb_lines:
                    break
