#!/usr/bin/python3
from sys import argv
save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file
filename = "add_item.json"
"""
adds arguments to a list then saves to file
"""
try:
    jsonlist = load_from_json_file(filename)
except:
    with open(filename, 'w', encoding='utf_8') as x:
        x.write('')
        jsonfile = []
jsonlist += sys.argv[1:]
save_to_json_file(jsonlist, filename)
