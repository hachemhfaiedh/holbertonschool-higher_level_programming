#!/usr/bin/python3
import hidden_4
if __name__ == '__main__':
    j = dir(hidden_4)
    for i in range(len(j)):
        if j[i][0] != "_":
            print(j[i])
