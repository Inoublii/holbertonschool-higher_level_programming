#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
	if type(first_name) != str:
		raise TypeError("first_name must be a string")
	if type(last_name) != str:
		raise TypeError("las_name must be a string")
	print("My name is", first_name, last_name)