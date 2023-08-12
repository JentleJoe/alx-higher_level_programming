#!/usr/bin/python3
def no_c(my_string):
    my_string = ''.join(characters for characters in my_string
                        if characters != 'c' and characters != 'C')

    return my_string
