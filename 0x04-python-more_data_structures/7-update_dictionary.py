#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds a key/value in a dictionary.

    Args:
        a_dictionary (dict): The input dictionary.
        key (str): The key to be added or replaced.
        value: The value associated with the key.
    """
    a_dictionary[key] = value
