#!/usr/bin/python3
""""Création d'une classe"""


class Square:
    """Classe représentant un carré avec une taille privée."""

    def __init__(self, size=0):
        """Initialise un carré avec une taille donnée.

        Args:
            size (int): La taille du côté du carré (doit être un entier >= 0).

        Raises:
            TypeError: Si size n'est pas un entier.
            ValueError: Si size est négatif.
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calcule et retourne l'aire du carré.

        Returns:
            int: L'aire du carré.
        """
        return self.__size * self.__size
