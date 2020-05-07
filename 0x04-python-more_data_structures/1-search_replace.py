#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    for i in my_list:
        if my_list[i] == search:
            new[i] = replace
    return new
