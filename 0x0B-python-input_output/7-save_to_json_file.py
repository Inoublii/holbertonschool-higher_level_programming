#!/usr/bin/python3
def save_to_json_file(my_obj, filename):
    import json
    with open(filename, "s", encoding="utf-8") as x:
        json.dump(my_obj, x)
