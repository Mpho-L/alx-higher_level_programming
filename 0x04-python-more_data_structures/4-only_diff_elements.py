#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    Returns a set of elements present in only one set.

    Args:
        set_1 (set): The first set.
        set_2 (set): The second set.

    Returns:
        set: A set containing elements present in only one set.
    """
    diff_set = set()

    for element in set_1:
        if element not in set_2:
            diff_set.add(element)

    for element in set_2:
        if element not in set_1:
            diff_set.add(element)
    
    return diff_set
