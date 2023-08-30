#!/usr/bin/python3
""" defines a square """


class Square:
    """ A square Class """

    def __init__(self, size=0):
        """ Initializes the square class

        Args:
            size: the size of the square, it is met to be private

        Raises:
            ValueError: If 'size' is not an integer and if 'size' is
                less that zero

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """ A public instance method that computes area of the square """
        return (self.__size ** 2)
