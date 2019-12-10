#!/usr/bin/env python3
def fizzbuzz():
    for i in range(1, 101):
        if (i % 5 == 0) and (i % 3 == 0):
            print(end="FizzBuzz ")
        elif (i % 5 == 0):
            print(end="Buzz ")
        elif(i % 3 == 0):
            print(end="Fizz ")
        else:
            print(end="{} ".format(i))
