#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ft = tuple_a + (0, 0)
    st = tuple_b + (0, 0)
    x = ft[0] + st[0]
    y = ft[1] + st[1]
    return (x, y)
