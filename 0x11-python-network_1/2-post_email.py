#!/usr/bin/python3
from urllib import request
from urllib import parse
from sys import argv

if __name__ == '__main__':
	url = argv[1]
	email = argv[2]

	value = {"email": email}
	data = parse.urlencode(value)
	data = data.encode('utf-8')
	req = request.Request(url, data)
	with request.urlopen(req) as resp:
		res = resp.read()
		print(res.decode('utf-8'))
