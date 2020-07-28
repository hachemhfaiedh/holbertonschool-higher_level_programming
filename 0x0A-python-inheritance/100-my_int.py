#!/usr/bin/python3
"""Inheritance"""


class MyInt(int):
    """MyInt class"""
    def __init__(self, a):
        self.a = a

    def __eq__(self, b):
        return self.a != b

    def __ne__(self, b):
        return not self.__eq__(b)
