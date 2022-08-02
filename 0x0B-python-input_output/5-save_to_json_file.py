#!/usr/bin/python3
"""
saving object in json representation in files
"""

def save_to_json_file(my_obj, filename):
    """ function that saves my_obj to filename"""
    import json
    with open(filename, 'w', encoding="utf-8") as w:
        w.write(json.dumps(my_obj))