#!/usr/bin/python
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        first_el_a = tuple_a[0]
        second_el_a = 0
    elif len(tuple_a) > 2:
        first_el_a = tuple_a[0]
        second_el_a = tuple_a[1]
    else:
        first_el_a = tuple_a[0]
        second_el_a = tuple_a[1]
    if len(tuple_b) < 2:
        first_el_b = tuple_b[0]
        second_el_b = 0
    elif len(tuple_b) > 2:
        first_el_b = tuple_b[0]
        second_el_b = tuple_b[1]
    else:
        first_el_b = tuple_b[0]
        second_el_b = tuple_b[1]
    last_tuple_1 = first_el_a + first_el_b
    last_tuple_2 = second_el_a + second_el_b
    last_tuple = (last_tuple_1, last_tuple_2)
    return last_tuple
if __name__ == "__main__":
    print(add_tuple((5,), (10, 20, 30)))