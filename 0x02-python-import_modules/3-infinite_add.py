#!/usr/bin/python3
from sys import argv
inf = 0
if __name__ == '__main__':
    for i in range(1, len(argv)):
        inf += int(argv[i])
    print("{}".format(inf))
