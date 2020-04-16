#!/usr/bin/python3
import requests
import sys
"""
Python script that takes in a URL and an email address, sends a POST request to
the passed URL with the email as a parameter, and finally displays the body of
the response.
"""
if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 1:
        q = ""
    elif len(sys.argv) == 2:
        q = sys.argv[1]
    res = requests.post(url, data={"q": q})
    try:
        j = res.json()
        if bool(j):
            print("[{}] {}".format(j["id"], j["name"]))
        else:
            print("No result")
            exit()
    except ValueError:
        print("Not a valid JSON")
