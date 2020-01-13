#!/usr/bin/python3
def text_indentation(text):
	if type(text) != str:
		raise TypeError("text must be a string")
	l = "\n"
	for i in text:
		if i == "." or i == "?" or i == ":":
			i += l 
		print(i, end="")
