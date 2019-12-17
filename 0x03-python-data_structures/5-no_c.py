#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        noC = ""
        for x in my_string:
            if x != 'C' and x != 'c':
                noC += x
        return noC
    else:
        return my_string
