#!/usr/bin/python3
""" MyList func """


class MyList(list):
    """ class that inhetits from list """
    def print_sorted(self):
        print(sorted(self))
