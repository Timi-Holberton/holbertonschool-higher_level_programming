#!/usr/bin/python3
"""
Module contenant une classe de base pour la géométrie.
"""


class BaseGeometry:
    """
    Classe de base destinée à servir de fondation pour les classes
    de formes géométriques.
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        self.value = value
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
