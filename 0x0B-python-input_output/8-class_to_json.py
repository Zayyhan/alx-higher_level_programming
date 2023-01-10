#!/usr/bin/python3

def class_to_json(obj):
    """creates a json representation of an object without
       importing any module
    """
     return repr({key: value for (key, value) in obj.__dict__.items()
                  if key in list(obj.__dict__.keys())})
