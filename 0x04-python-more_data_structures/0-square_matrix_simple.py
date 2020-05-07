#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = [list(map(lambda i: i*i, j)) for i in matrix]
    return square
