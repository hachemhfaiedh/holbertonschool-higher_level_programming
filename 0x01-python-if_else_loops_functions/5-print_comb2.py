#!/usr/bin/python3
for comb in range(0, 100):
    if comb != 99:
        print("{:02d}, ".format(comb), end="")
    if comb == 99:
        print(comb)
