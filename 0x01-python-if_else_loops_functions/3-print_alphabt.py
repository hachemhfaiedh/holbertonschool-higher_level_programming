#!/usr/bin/python3
for ab in range(97, 123):
    if ab == 101 or ab == 113:
        continue
    else:
        print("{}".format(chr(ab)), end="")
