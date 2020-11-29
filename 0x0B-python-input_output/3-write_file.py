#!/usr/bin/python3
"""input output"""


def write_file(filename="", text=""):
    """write a text file"""

    text_file = open(filename, "w")
    n = text_file.write(text)
    return n
