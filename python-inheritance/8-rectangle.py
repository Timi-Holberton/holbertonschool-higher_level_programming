#!/usr/bin/python3
"""
Définition de classes pour la géométrie.

Ce module contient une classe de base `BaseGeometry` servant de modèle
abstrait pour des formes géométriques, ainsi qu'une classe `rectangle`
dérivée qui représente un rectangle.

La classe `BaseGeometry` propose une méthode `area` à surcharger, ainsi
qu’un validateur d’entiers strictement positifs.

La classe `rectangle` hérite de `BaseGeometry` et permet de définir un
rectangle via sa largeur et sa hauteur.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Classe représentant un rectangle, dérivée de BaseGeometry.

    Constructeur :
        __init__(name, value, width, height)
            Initialise une instance de rectangle avec un nom, une valeur,
            une largeur et une hauteur.

    Attributs privés :
        __width (int) : Largeur du rectangle.
        __height (int) : Hauteur du rectangle.

    Notes :
        La validation de largeur et hauteur peut être effectuée
        avec la méthode integer_validator héritée de BaseGeometry,
        mais elle n’est pas appliquée dans ce constructeur tel quel.
    """

    def __init__(self, width, height):
        """
        Initialise un rectangle avec un nom, une valeur, une largeur
        et une hauteur.

        Args :
        name (str) : Nom pour la validation (non utilisé ici directement)
        value (int) : Valeur pour la validation (non utilisée ici directement)
        width (int) : Largeur du rectangle.
        height (int) : Hauteur du rectangle.
        """
        self.integer_validator("height", height)
        self.integer_validator("hwidth", width)
        self.__width = width
        self.__height = height
