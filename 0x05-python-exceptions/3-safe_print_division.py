#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        h = a / b
    except ZeroDivisionError:
        h = None
    finally:
        print("Inside result: {}".format(h))
        return h
