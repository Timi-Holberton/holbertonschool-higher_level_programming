#!/usr/bin/python3
"""
Définition de classes pour la géométrie.

Ce module contient une classe de base `BaseGeometry` servant de modèle
abstrait pour des formes géométriques, ainsi qu'une classe `Rectangle`
dérivée qui représente un rectangle.

La classe `BaseGeometry` propose une méthode `area` à surcharger, ainsi
qu’un validateur d’entiers strictement positifs.

La classe `Rectangle` hérite de `BaseGeometry` et permet de définir un
rectangle via sa largeur et sa hauteur.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Classe représentant un rectangle, dérivée de BaseGeometry.

    Constructeur :
        __init__(width, height)
        Initialise une instance de rectangle avec une largeur et une hauteur.

    Attributs privés :
        __width (int) : Largeur du rectangle.
        __height (int) : Hauteur du rectangle.

    Notes :
        La validation de largeur et hauteur est effectuée
        avec la méthode integer_validator héritée de BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initialise un rectangle avec une largeur et une hauteur.

        Args :
            width (int) : Largeur du rectangle.
            height (int) : Hauteur du rectangle.
        """
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calcule et retourne l'aire du rectangle.

        Returns :
            int : Aire du rectangle (largeur × hauteur).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Retourne une représentation textuelle du rectangle.

        Returns :
            str : Chaîne formatée [Rectangle] <largeur>/<hauteur>.
        """
        return str(f"[Rectangle] {self.__width}/{self.__height}")
