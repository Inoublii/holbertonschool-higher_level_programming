#!/usr/bin/python3
"""Module add_integer method."""
def add_integer(a, b=98):
	 """Adds two integers.
	 ints:
        a: integer.
        b: integer, default 98.
    Raises:
        TypeError: if a, b are not int, float.
    Returns:
        The sum
    """
	if type(a) == float:
		a = int(a)
	if type(b) == float:
		b = int(b)
	if type(a) is not int and type(a) is not float:
		raise TypeError("a must be an integer")
	elif type(b) is not int and type(b) is not float:
		raise TypeError("b must be an integer")
	return a + b
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
