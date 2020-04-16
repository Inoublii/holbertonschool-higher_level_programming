#!/usr/bin/python3
"""
 Displays last 10 commits informations.
"""
import requests
import sys

if __name__ == "__main__":

    rep = sys.argv[1]
    user = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(user, rep)
    req = requests.get(url)
    commits = req.json()[:10]
    for com in commits:
        res = com.get('commit').get('author').get('name')
        sha = com.get('sha')
        print('{}: {}'.format(sha, res))




