#!/usr/bin/python3

class Rectangle:
    """Classe représentant un rectangle géométrique.

    Permet de définir un rectangle avec une largeur et une hauteur,
    incluant les vérifications de type et de valeur.
    """

    def __init__(self, width=0, height=0):
        """Initialise un rectangle avec une largeur et une hauteur.

        Args:
            width (int): Largeur du rectangle (par défaut 0).
            height (int): Hauteur du rectangle (par défaut 0).

        Raises:
            TypeError: Si width ou height n'est pas un entier.
            ValueError: Si width ou height est négatif.
        """
        self.width = width
        self.height = height

    def area(self):
        """Calcule et retourne l'aire du rectangle.

        Returns:
            int: L'aire, calculée comme width * height.
        """
        return self.width * self.height

    def perimeter(self):
        """Calcule et retourne le périmètre du rectangle.

        Returns:
            int: Le périmètre, calculé comme 2 * (width + height).
                 Retourne 0 si l'une des dimensions est nulle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    @property
    def width(self):
        """Récupère la largeur du rectangle.

        Returns:
            int: La largeur actuelle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Définit la largeur du rectangle.

        Args:
            value (int): La nouvelle largeur à définir.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est négatif.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Récupère la hauteur du rectangle.

        Returns:
            int: La hauteur actuelle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Définit la hauteur du rectangle.

        Args:
            value (int): La nouvelle hauteur à définir.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est négatif.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """Renvoie une représentation en chaîne du rectangle."""
        if self.width == 0 or self.height == 0:
            return ""
        lignes = ["#" * self.width for _ in range(self.height)]
        return "\n".join(lignes)

    def __repr__(self):
       """Renvoie une représentation en chaîne du rectangle.
       """
       return f"Rectangle({self.width}, {self.height})"
