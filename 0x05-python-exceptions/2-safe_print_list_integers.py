#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        h = 0
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                h += 1
        print()
        return(h)
    except(TypeError, ValueError):
        pass
