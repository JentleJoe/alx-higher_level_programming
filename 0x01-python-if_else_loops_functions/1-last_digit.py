#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if (number < 0):
    last = last * (-1)
if (last < 6 and last != 0):
    print('Last digit of', number, 'is', last, 'and is less than 6 and \
not 0')
elif (last == 0):
    print('Last digit of', number, 'is', last, 'and is 0')
elif (last > 5):
    print('Last digit of', number, 'is', last, 'and is greater than 5')
