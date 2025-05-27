#!/usr/bin/python3
"""
Définition de classes pour la géométrie.

Ce module contient une classe de base `BaseGeometry` servant de modèle
abstrait pour des formes géométriques, ainsi qu'une classe `Rectangle`
et une classe `Square` dérivée de `Rectangle`.

La classe `BaseGeometry` propose une méthode `area` à surcharger, ainsi
qu’un validateur d’entiers strictement positifs.

La classe `Rectangle` permet de définir un rectangle via sa largeur et
sa hauteur.

La classe `Square` hérite de `Rectangle` et permet de définir un carré
à partir de la taille d’un seul côté.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Classe représentant un carré, dérivée de Rectangle.

    Constructeur :
        __init__(size)
            Initialise une instance de carré avec une taille unique.

    Attributs privés :
        __size (int) : Taille d’un côté du carré.

    Notes :
        La taille est validée à l’aide de la méthode integer_validator
        héritée de BaseGeometry.
    """

    def __init__(self, size):
        """
        Initialise un carré avec une taille.

        Args :
            size (int) : Taille d’un côté du carré.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Calcule et retourne l'aire du carré.

        Returns :
            int : Aire du carré (size × size).
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Retourne une représentation textuelle du carré.

        Returns :
            str : Chaîne formatée [Square] <size>/<size>.
        """
        return str(f"[Square] {self.__size}/{self.__size}")
