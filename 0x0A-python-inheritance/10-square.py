#!/usr/bin/python3
"""Inheritance"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(self.__size, self.__size)
