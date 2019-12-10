#!/usr/bin/python3
for i in range(97, 122):
    if not i == 101 and not i == 113:
        print('{:c}'.format(i), end="")
