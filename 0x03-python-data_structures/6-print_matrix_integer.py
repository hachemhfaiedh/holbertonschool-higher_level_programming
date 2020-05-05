#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    a = len(matrix)
    b = len(matrix[i])
    for i in range(a):
        for j in range(b):
            print("{:d}".format(matrix[i][j]), end="")
            if j < b - 1):
                print(end=" ")
        print()
