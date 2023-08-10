#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if (len(str) == 0):
            break
        if (ord(str[i]) >= 97 and ord(str[i]) <= 122):
            char = chr(ord(str[i]) - 32)
        else:
            char = chr(ord(str[i]))
        if (i == len(str) - 1):
            print("{}".format(char))
            break
        print("{}".format(char), end='')
