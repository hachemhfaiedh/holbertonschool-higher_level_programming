#!/usr/bin/python3
"""is_same_class func"""


def is_same_class(obj, a_class):
    """checks if object is exactly an instance of the specified class"""
    if type(obj) is a_class:
        return True
    else:
        return False
