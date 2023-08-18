#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list (only once for each integer).

    Args:
        my_list (list): The input list.

    Returns:
        int: The sum of unique integers in the list.
    """
    unique_numbers = set()
    total_sum = 0
    
    for num in my_list:
        if num not in unique_numbers:
            unique_numbers.add(num)
            total_sum += num
    
    return total_sum
