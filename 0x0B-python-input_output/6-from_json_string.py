#!/usr/bin/python3
"""input output"""


import json


def from_json_string(my_str):
    """return obj represented by JSON string"""
    return json.loads(my_str)
