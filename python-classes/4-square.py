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

    @property
    def size(self):
        """Getter : retourne la taille du carré.

    Returns:
        int: La taille du carré (valeur de __size).
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter : définit la taille du carré avec vérification.

    Args:
        value (int): La nouvelle taille du carré.

    Raises:
        TypeError: Si la valeur n'est pas un entier.
        ValueError: Si la valeur est négative.
    """
        self.__size = value

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")
