#!/usr/bin/python3
def max_integer(my_list=[]):
     """Finds the biggest integer in a list."""
    if not my_list:  # empty list
        return None

    max_val = my_list[0]  # assume first element is the largest
    for num in my_list:
        if num > max_val:
            max_val = num
    return max_val
