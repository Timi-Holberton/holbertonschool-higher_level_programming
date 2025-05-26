#!/usr/bin/python3
"""
Module contenant une classe de base pour la géométrie.
"""


class BaseGeometry:
    """
    Classe de base destinée à servir de fondation pour les classes
    représentant des formes géométriques.

    Cette classe fournit une interface générale avec une méthode
    'area' non implémentée, et une méthode utilitaire
    'integer_validator' pour valider les attributs entiers positifs.
    """

    def area(self):
        """
        Calcule l'aire de la forme géométrique.

        Cette méthode doit être implémentée par les classes filles.
        Si elle n'est pas redéfinie, elle lève une exception.

        Raises:
            Exception: Toujours levée pour indiquer que la méthode
            n'est pas implémentée.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valide que la valeur donnée est un entier strictement positif.

        Args:
            name (str): Nom de l'attribut à valider
            (utilisé dans le message d'erreur).
            value (int): Valeur à valider.

        Raises:
            TypeError: Si 'value' n'est pas un entier.
            ValueError: Si 'value' est inférieur ou égal à 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
