#!/usr/bin/python3
""" defines a square """


class Square:
    """ A square Class """

    def __init__(self, size=0):
        """ Initializes the square class

        Args:
            __size: the size of the square, it is met to be private

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")

        self.__size = size
