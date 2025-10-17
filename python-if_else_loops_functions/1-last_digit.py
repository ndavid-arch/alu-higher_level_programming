#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    l_digit = int(str(number)[-1]) * -1
else:
    l_digit = int(str(number)[-1])
if l_digit > 5:
    print("Last digit of", number, "is", l_digit, "and is greater than 5")
elif l_digit == 0:
    print("Last digit of", number, "is", l_digit, "and is 0")
elif l_digit < 6 and l_digit != 0:
    print("Last digit of", number, "is", l_digit,
          "and is less than 6 and not 0")
