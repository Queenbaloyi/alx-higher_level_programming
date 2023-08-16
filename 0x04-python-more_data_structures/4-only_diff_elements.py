#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Return a set of all elements present in only one set.

    Args:
        set_1 (set): The first set.
        set_2 (set): The second set.

    Returns:
        set: A set of all elements present in only one set.
    """

    only_diff_elements = set(set_1) ^ set(set_2)
    return only_diff_elements
