#!/usr/bin/python3
def uppercase(str):
    for x in range(len(str)):
        a = ord(str[x])
        if a >= 97 and a <= 123:
            a -= 32
        print(end="{}".format(chr(a)))
    print()
