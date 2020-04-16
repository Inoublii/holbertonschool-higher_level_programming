#!/usr/bin/python3
import requests
import sys
"""
Python script that takes your Github credentials
(username and password) and uses the Github API to display your id
"""
if __name__ == "__main__":
    dic = {}
    dic['username'] = sys.argv[1]
    dic['Authorization'] = 'token ' + sys.argv[2]
    rs = requests.get('https://api.github.com/user', headers=dic)
    jsn = rs.json()
    if rs.status_code == 200:
        print(jsn['id'])
    else:
        print('None')
