#!/usr/bin/python3
""""Création d'une class"""


class Square:
    """Ma classe"""
    pass

    def __init__(self, size=0):
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")
