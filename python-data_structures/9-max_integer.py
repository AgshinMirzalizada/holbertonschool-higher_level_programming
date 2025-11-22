#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) > 0:
        sort_list = sort(my_list)
        max_value = sort_list[-1]
    else:
        return None
