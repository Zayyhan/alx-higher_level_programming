#!/usr/bin/python3
"""module for deserializing json data back to python objects
"""


import json


def to_json_string(my_obj):
    """The json representation of an object (string)
    -> handles no exceptions in serialization proccess
    """
    return json.dumps(my_obj)
