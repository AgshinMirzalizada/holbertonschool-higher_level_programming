#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) > 0:
        sort_list = sorted(my_list)
        max_value = sort_list[-1]
        return max_value
    else:
        return None
