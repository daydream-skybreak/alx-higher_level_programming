#!/usr/bin/python3
"""
module for returning object from json file
"""


def load_from_json_file(filename):
    """ function for returning object from json file"""
    import json
    with open(filename, encoding="utf-8") as f:
        return json.loads(f.read())
