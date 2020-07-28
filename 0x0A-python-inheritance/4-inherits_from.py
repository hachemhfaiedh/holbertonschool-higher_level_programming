#!/usr/bin/python3
"""Inheritance"""


def inherits_from(obj, a_class):
    """inherits from func"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
