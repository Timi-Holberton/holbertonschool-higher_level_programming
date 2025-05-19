#!/usr/bin/python3
""""Création d'une classe"""


class Square:
    """Classe représentant un carré avec une taille + une position privées."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialise un carré avec une taille et une position données.

        Args:
            size (int): La taille du côté du carré (doit être un entier >= 0).
            position (tuple): Position du carré (tuple de 2 entiers positifs).

        Raises:
            TypeError: Si size pas un entier, ou si position est invalide.
            ValueError: Si size est négatif.
        """
        self.size = size
        self.position = position

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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter : retourne la position du carré.

        Returns:
            tuple: La position du carré (tuple de 2 entiers positifs).
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter : définit la position du carré avec vérification.

        Args:
            value (tuple): La nouvelle position (2 entiers positifs).

        Raises:
            TypeError: Si value n'est pas un tuple de 2 entiers positifs.
        """
        if (not isinstance(value, tuple) or len(value) != 2
           or not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Affiche le carré avec des # en tenant compte de la position."""
        if self.size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
