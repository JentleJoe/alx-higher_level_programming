#!/usr/bin/python3
i = 1
for char in range (ord('z'), ord('a') - 1, -1):
    if (i % 2 == 0):
        char = chr(char).upper()
    print(chr(char), end='')
    i = i + 1
