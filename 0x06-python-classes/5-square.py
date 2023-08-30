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
            raise ValueError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """ Gets the size attribute value

        Returns:
            the size attribute's value

        """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the size attribute

        Args:
            value: value to set the size to

        Raises:
            ValueError: If 'size' is not an integer and if 'size' is
                less that zero

        """
        if not isinstance(value, int):
            raise ValueError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ A public instance method that computes area of the square """

        return self.__size ** 2

    def my_print(self):
        """ Prints square with character '#' to stdout

        If size == 0, an empty line is printed

        """
        if (self.size == 0):
            print('\n')
        else:
            for num in range(self.size):
                for char in range(self.size):
                    print("#", end='')
                print()
