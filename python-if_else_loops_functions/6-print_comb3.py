#!/usr/bin/python3
for x in range(10):
    for y in range(10):
        if (x == 8 and y == 9):
            print("{}".format(str(x) + str(y)))
        elif (y > x):
            print("{}".format(str(x) + str(y)) + ', ', end='')
