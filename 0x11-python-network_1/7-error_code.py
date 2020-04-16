#!/usr/bin/python3
import sys
import requests

if __name__ == '__main__':
    try:
        url = sys.argv[1]
        req = requests.get(url)
        stat = req.status_code
        check = req.raise_for_status()
        print(req.text)
    except requests.exceptions.HTTPError:
        print("Error code:", stat)
