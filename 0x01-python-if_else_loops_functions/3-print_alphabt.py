#!/usr/bin/python3
for characters in range(ord('a'), ord('z') + 1):
    if (chr(characters) == 'e' or chr(characters) == 'q'):
        continue
    print("{}".format(chr(characters)), end='')
