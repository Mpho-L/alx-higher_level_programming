#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers in a matrix.

    Args:
    matrix (list of list): A 2D array containing integers.

    Returns:
    list of list: A new matrix with each value squared.
    """
    squared_matrix = []

    for row in matrix:
        squared_row = []
        for element in row:
            squared_row.append(element ** 2)
        squared_matrix.append(squared_row)
    
    return squared_matrix
