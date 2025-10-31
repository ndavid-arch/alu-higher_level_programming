#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        # Join each integer in the row with a space using str.format
        print(" ".join("{:d}".format(num) for num in row))
