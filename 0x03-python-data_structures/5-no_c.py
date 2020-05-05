#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    if my_string:
        for char in range(len(my_string)):
            if new_string[char] not in 'Cc':
                new_string = new_string + my_string[char]
    return (new_string)
