#!/usr/bin/python3
"""input output"""


import json


def load_from_json_file(filename):
    """load from json file"""
    with open(filename) as f:
        return json.load(f)
