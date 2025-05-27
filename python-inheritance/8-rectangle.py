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


class BaseGeometry:
    """
    Classe de base pour la géométrie.

    Fournit une interface générique pour les formes géométriques.

    Méthodes :
        area() : Doit être surchargée. Lève une exception si appelée.
        integer_validator(name, value) : Valide que value est un int > 0.
    """

    def area(self):
        """
        Méthode qui doit être surchargée dans les classes dérivées.
        Lève une exception si appelée directement.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valide que 'value' est un entier strictement positif.

        Args:
            name (str): Le nom de la variable à valider
                        (utilisé dans les messages d'erreur).
            value: La valeur à valider.

        Raises:
            TypeError: Si value n'est pas un entier (exclut les booléens).
            ValueError: Si value est inférieur ou égal à 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


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
        self.integer_validator(width, height)
        self.__width = width
        self.__height = height
