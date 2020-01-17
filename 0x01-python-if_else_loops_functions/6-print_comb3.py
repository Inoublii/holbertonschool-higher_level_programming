#!/usr/bin/python3
for i in range(0, 10):
    for x in range(0, 10):
        if i < x and i != 8:
            print("{}{}, ".format(i, x), end='')
print("89")
