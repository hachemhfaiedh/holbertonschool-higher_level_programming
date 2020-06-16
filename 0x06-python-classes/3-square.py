#!/usr/bin/python3
"""defining classes"""


class Square:
    """square class with no attributes"""
    def __init__(self, size=0):
        """Instantiation with size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """square area"""
        return self.__size * self.__size
