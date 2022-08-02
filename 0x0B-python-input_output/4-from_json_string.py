#!/usr/bin/python3
"""
module to decode json strings
"""


def from_json_string(my_str):
    """function that decodes json strings"""
    import json
    return json.loads(my_str)
