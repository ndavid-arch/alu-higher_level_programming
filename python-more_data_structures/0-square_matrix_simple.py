#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Returns a new matrix with all values squared."""
    # Use a list comprehension to create a new matrix
    return [[value ** 2 for value in row] for row in matrix]
