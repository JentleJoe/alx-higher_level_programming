#!/usr/bin/python3
i = 1
for char in range(ord('z'), ord('a') - 1, -1):
    if (i % 2 == 0):
        char = char - 32
    print("{}".format(chr(char)), end='')
    i = i + 1
