#!/usr/bin/python3
def load_from_json_file(filename):
    import json
    with open(filename, encoding='utf-8') as x:
        return json.load(x)
