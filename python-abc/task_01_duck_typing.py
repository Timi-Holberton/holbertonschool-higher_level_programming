#!/usr/bin/env python3
"""
Module de formes géométriques utilisant les classes abstraites.

Ce module définit une hiérarchie de classes pour représenter des formes
géométriques comme le cercle et le rectangle, en utilisant le module `abc`
pour définir une interface commune (Shape) avec des méthodes abstraites.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Classe abstraite représentant une forme géométrique.

    Méthodes abstraites :
        area() -> float : Calcule et retourne l'aire de la forme.
        perimeter() -> float : Calcule et retourne le périmètre de la forme.
    """

    @abstractmethod
    def area(self):
        """Calcule et retourne l'aire de la forme."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calcule et retourne le périmètre de la forme."""
        pass


class Circle(Shape):
    """
    Classe représentant un cercle.

    Attributs :
        radius (float) : Rayon du cercle.

    Méthodes :
        area() -> float : Retourne l'aire du cercle.
        perimeter() -> float : Retourne le périmètre du cercle.
    """

    def __init__(self, radius):
        """
        Initialise un cercle avec un rayon donné.

        Args :
            radius (float) : Rayon du cercle (valeur absolue utilisée).
        """
        self.radius = abs(radius)

    def area(self):
        """Calcule et retourne l'aire du cercle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calcule et retourne le périmètre du cercle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Classe représentant un rectangle.

    Attributs :
        width (float) : Largeur du rectangle.
        height (float) : Hauteur du rectangle.

    Méthodes :
        area() -> float : Retourne l'aire du rectangle.
        perimeter() -> float : Retourne le périmètre du rectangle.
    """

    def __init__(self, width, height):
        """
        Initialise un rectangle avec une largeur et une hauteur.

        Args :
            width (float) : Largeur du rectangle (valeur absolue utilisée).
            height (float) : Hauteur du rectangle (valeur absolue utilisée).
        """
        self.width = abs(width)
        self.height = abs(height)

    def area(self):
        """Calcule et retourne l'aire du rectangle."""
        return self.height * self.width

    def perimeter(self):
        """Calcule et retourne le périmètre du rectangle."""
        return 2 * (self.width + self.height)

if __name__ == "__main__":
    def shape_info(Shape):
        """
        Affiche l'aire et le périmètre d'une forme géométrique.

        Args :
            Shape (Shape) : Instance d'une classe dérivée de Shape.
        """
        print("Area:", Shape.area())
        print("Perimeter:", Shape.perimeter())
