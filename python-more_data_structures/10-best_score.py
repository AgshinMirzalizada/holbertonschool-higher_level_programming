#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    else:
        max = None
        for key in a_dictionary:
            if a_dictionary[key] > max:
                max = a_dictionary[key]
                max_key = key
        return max_key
