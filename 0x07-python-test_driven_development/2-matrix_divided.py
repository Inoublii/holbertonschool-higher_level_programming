#!/usr/bin/python3
def matrix_divided(matrix, div):
	new = []
	for i in range(matrix):
		new += matrix[i] / div
	return new
