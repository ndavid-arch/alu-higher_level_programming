#!/usr/bin/python3
"""Define a function that reads text files."""
def read_file(filename=""):
    """A function to read a text file."""
    with open(filename, 'r', encoding='UTF8') as b:
        print(b.read(), end='')
