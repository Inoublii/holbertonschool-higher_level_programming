#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of ", end='')
if number > 0 and number % 10 > 5:
    print("{} is {} and is greater than 5".format(number, number % 10))
elif number % 10 == 0:
    print("{} is {} and is 0".format(number, number % 10))
elif number < 0:
    print("{} is {} and is less than 6 and not 0".format(number, number % -10))
