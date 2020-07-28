#!/usr/bin/python3
"""Inheritance"""


def add_attribute(obj, attr, value):
    """add attribute func"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
