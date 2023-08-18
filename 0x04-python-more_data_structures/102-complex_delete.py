def complex_delete(a_dictionary, value):
    """
    Deletes keys with a specific value from a dictionary.

    Args:
        a_dictionary (dict): The input dictionary.
        value: The value to search for and delete.

    Returns:
        None: The function modifies the dictionary in place.
    """
    keys_to_delete = [key for key, val in a_dictionary.items() if val == value]
    for key in keys_to_delete:
        del a_dictionary[key]
