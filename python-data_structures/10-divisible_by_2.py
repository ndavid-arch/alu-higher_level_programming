#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list and returns a list of True/False."""
    result = []
    for num in my_list:
        result.append(num % 2 == 0)
    return result
