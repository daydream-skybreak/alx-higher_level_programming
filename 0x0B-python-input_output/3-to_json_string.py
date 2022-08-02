#!/usr/bin/python3
"""
module for returning json representation of objects
"""


import mailbox


def to_json_string(my_obj):
    """ function to return json representation of objects """
    import json
    return json.dumps(my_obj)
