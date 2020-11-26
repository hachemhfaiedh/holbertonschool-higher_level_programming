#!/usr/bin/python3
"""inout/output"""


def read_file(filename=""):
    """read n print file"""
    with open("{}".format(filename)) as f:
            print(f.read(), end="")
