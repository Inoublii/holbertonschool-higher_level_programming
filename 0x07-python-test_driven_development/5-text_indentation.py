#!/usr/bin/python3
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
    """text_indentation"""


def text_indentation(text):
	"""add 2 new lines after '.?:'
    str:
        text: str
    Raises:
        TypeError: If text is not str
    """
	if type(text) != str:
		raise TypeError("text must be a string")
	l = ".?:"
	for x in l:
		text = (x + "\n\n").join([a.strip(" ") for a in text.split(x)])
	print(text, end="")
