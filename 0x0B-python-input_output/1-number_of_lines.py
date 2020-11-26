#!/usr/bin/python3
"""input output"""


def number_of_lines(filename=""):
    """nb of line in txt file"""
    i = 0
    with open("{}".format(filename)) as f:
        for line in f:
            i += 1
    return i
