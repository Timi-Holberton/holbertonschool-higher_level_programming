#!/usr/bin/python3

class BaseGeometry:
    """
    Classe de base pour la géométrie.
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
