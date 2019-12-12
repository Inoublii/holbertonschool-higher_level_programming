#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    x = 0
    if len(argv) == 1:
        print("0 arguments.")
        exit()
    a = len(argv) - 1
    if len(argv) == 2:
        print('{} argument:'.format(a))
    else:
        print('{} arguments:'.format(a))
    for e in argv:
        x += 1
        if x == 1:
            continue
        print('{}: {}'.format(x - 1, e))
