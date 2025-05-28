#!/usr/bin/env python3

"""
Définition de classes représentant différents types d'animaux
et leurs comportements.

Ce module inclut trois classes :
- Fish : représente un poisson.
- Bird : représente un oiseau.
- FlyingFish : représente un poisson volant,
combinant les caractéristiques des deux.

Chaque classe implémente des comportements spécifiques tels que nager,
voler et décrire leur habitat.
"""


class Fish:
    """
    Représente un poisson avec la capacité de nager
    et un habitat aquatique.

    Méthodes:
        swim(): Affiche que le poisson nage.
        habitat(): Affiche l'habitat naturel du poisson.
    """

    def swim(self):
        """
        Affiche un message indiquant que le poisson nage.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Affiche un message décrivant l'habitat naturel du poisson.
        """
        print("The fish lives in water")


class Bird:
    """
    Représente un oiseau avec la capacité de voler et un habitat aérien.

    Méthodes:
        fly(): Affiche que l'oiseau vole.
        habitat(): Affiche l'habitat naturel de l'oiseau.
    """

    def fly(self):
        """
        Affiche un message indiquant que l'oiseau vole.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Affiche un message décrivant l'habitat naturel de l'oiseau.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Représente un poisson volant, combinant les capacités de nager
    et de voler.

    Hérite des classes Fish et Bird,
    et redéfinit les méthodes pour refléter son double habitat.

    Méthodes:
        fly(): Affiche que le poisson volant plane dans les airs.
        swim(): Affiche que le poisson volant nage.
        habitat(): Affiche l'habitat combiné (eau et ciel).
    """

    def fly(self):
        """
        Affiche un message indiquant que le poisson volant plane
        dans les airs.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Affiche un message indiquant que le poisson volant nage.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Affiche un message décrivant l'habitat combiné du poisson volant.
        """
        print("The flying fish lives both in water and the sky!")
