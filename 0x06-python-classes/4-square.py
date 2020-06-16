#!/usr/bin/python3
"""defining classes"""


class Square:
    """square class with no attributes"""
    def __init__(self, size=0):
        """Instantiation with size"""
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """square area"""
        return self.__size * self.__size
