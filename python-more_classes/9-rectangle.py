#!/usr/bin/python3
""""Création d'une classe pour définir un rectangle"""


class Rectangle:
    """Classe représentant un rectangle géométrique.

    Permet de définir un rectangle avec une largeur et une hauteur,
    incluant les vérifications de type et de valeur.
    """

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

    @classmethod
    def square(cls, size=0):
        """
        Crée une nouvelle instance de Rectangle où la largeur et
        la hauteur sont égales à size.

        Args:
            size (int): La taille des côtés du carré.

        Returns:
            Rectangle: Une nouvelle instance avec width == height == size.
        """
        return cls(size, size)

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare deux rectangles et retourne le plus grand en surface.

        Si les deux rectangles ont la même surface, retourne rect_1.

        Args:
            rect_1 (Rectangle): Le premier rectangle à comparer.
            rect_2 (Rectangle): Le deuxième rectangle à comparer.

        Raises:
           TypeError: Si rect_1 ou rect_2 n'est pas une instance de Rectangle.

        Returns:
            Rectangle: Le rectangle ayant la plus grande aire,
            ou rect_1 en cas d'égalité.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

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
        lignes = [str(self.print_symbol) * self.width
                  for _ in range(self.height)]
        return "\n".join(lignes)

    def __repr__(self):
        """Renvoie une chaîne de caractères qui permet de recréer un nouvel
        objet identique.

        Returns:
            str: Une représentation officielle du rectangle sous la forme
                Rectangle(width, height), utilisable avec eval().
        """
        eval(f"Rectangle({self.width}, {self.height})")

    def __del__(self):
        """Appelée automatiquement lors de la destruction de l'objet.

        Affiche un message d'adieu quand une instance de Rectangle
        est supprimée (par le ramasse-miettes ou avec 'del').
        """
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
        print("Bye rectangle...")
