#!/usr/bin/python3
"""Module for say_my_name ."""
def say_my_name(first_name, last_name=""):
 """printing first and last name
  str:
   first_name: first name
   last_name: last name
Raises:
     TypeError: If first_name or last_name are not strings.
  """
	if type(first_name) != str:
		raise TypeError("first_name must be a string")
	if type(last_name) != str:
		raise TypeError("las_name must be a string")
	print("My name is", first_name, last_name)
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
