#!/usr/bin/python3
def uppercase(str):
    uppercase = 0
    for x in str:
        if ord(x) >= 97 and ord(x) <= 122:
            uppercase = 32
        else:
            uppercase = 0
        print("{}".format(chr(ord(x) - uppercase)), end='')
    print()
