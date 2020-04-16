#!/usr/bin/python3
from urllib import request
"""Python script that fetches https://intranet.hbtn.io/status"""
if __name__ == '__main__':
    with request.urlopen('https://intranet.hbtn.io/status') as resp:
        data = resp.read()
    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content:{}"
          .format(type(data), data, data.decode('utf-8')))
