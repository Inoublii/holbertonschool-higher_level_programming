#!/usr/bin/python3
def add_integer(a, b=98):
	if type(a) == float:
		a = int(a)
	if type(b) == float:
		b = int(b)
	if type(a) is not int and type(a) is not float:
		raise TypeError("a must be an integer")
	elif type(b) is not int and type(b) is not float:
		raise TypeError("b must be an integer")
	return a + b
