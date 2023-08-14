#!/usr/bin/python3
# 7-add_tuple.py

def add_tuple(my_tuple_a=(), tuple_b=()):
    """Add two tuples."""
    my_tuple_a += (1,)

    if len(my_tuple_a) < 2:
        if len(my_tuple_a) == 0:
            my_tuple_a = 0, 0
        else:
            my_tuple_a = my_tuple_a[0], 0
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0

    return (my_tuple_a[0] + tuple_b[0], my_tuple_a[1] + tuple_b[1])
