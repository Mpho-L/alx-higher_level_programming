#!/usr/bin/python3

def number_keys(a_dictionary):
    """
    Returns the number of keys in a dictionary.

    Args:
        a_dictionary (dict): The input dictionary.

    Returns:
        int: The number of keys in the dictionary.
    """
    num_keys = 0
    for key in a_dictionary:
        num_keys += 1
    return num_keys
