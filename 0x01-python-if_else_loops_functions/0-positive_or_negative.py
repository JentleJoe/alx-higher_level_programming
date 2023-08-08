#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if (number % 10 > 0):
    print(number % 10, 'is positive')
elif (number % 10 < 0):
    print(number % 10, 'is negative')
else:
    print(number % 10, 'is zero')
