#!/usr/bin/python3
"""module for deserializing json data back to python objects
"""

import json

def from_json_string(my_str):
    """returns python object represented by a JSON string
    """
    return json.loads(my_str)
