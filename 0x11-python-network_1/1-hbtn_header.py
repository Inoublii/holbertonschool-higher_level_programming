#!/usr/bin/python3
from urllib import request
from urllib import parse
import sys
"""script that takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response."""


if __name__ == '__main__':
    req = request.Request(sys.argv[1])
    with request.urlopen(req) as resp:
        print(resp.info().get("X-Request-Id"))
