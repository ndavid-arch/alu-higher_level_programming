#!/usr/bin/python3
"""Create a square """


class Square:
    """
    Create a square
        Has a private Instance att: size
    """

    def __init__(self, size=0):
        """ init size """
        self.__size = size

    @property
    def size(self):
        """ returns the size att """
        return self.__size

    @size.setter
    def size(self, value):
        """ asign the size to the size att """
        if(type(value) is not int):
            raise TypeError("size must be an integer")
        if(value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return(self.__size**2)

    def my_print(self):
        if(self.size):
            for x in range(self.size):
                print("#" * self.size, end='')
                print()
        else:
            print()
