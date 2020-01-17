#!/usr/bin/python3
def matrix_divided(matrix, div):
	"""Divides matrix by div.
    vs:
        matrix: dictionairy
        div: number
    Returns:
        list: Dictionairy
    Raises:
        TypeError: If matrix is not list containing int or float.
        TypeError: If lists are not same size.
        TypeError: If div is not int or float.
        ZeroDivisionError: If div is zero.
    """
	new = []
	for i in range(matrix):
		new += matrix[i] / div
	return new
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
