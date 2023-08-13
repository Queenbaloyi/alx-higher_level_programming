#!/usr/bin/python3
# 2-replace_in_list.py

def replace_element_in_sequence(my_sequence, index, element):
    """Replace an element of a sequence at a specific position."""
    if index < 0 or index >= len(my_sequence):
        return my_sequence
    my_sequence_copy = my_sequence[:]
    my_sequence_copy[index] = element
    return my_sequence_copy
