#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new0 = []
    a = 0
    for i in range(list_length):
        try:
            a = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            a = 0
        except ZeroDivisionError:
            print("division by 0")
            a = 0
        except IndexError:
            print("out of range")
            a = 0
        finally:
            new0.append(a)
    return new0
