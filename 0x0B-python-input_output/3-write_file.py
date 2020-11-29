#!/usr/bin/python3
"""input output"""


def write_file(filename="", text=""):
    """write a text file"""

    with open(filename, "w") as f:
        n = f.write(text)
    return n
