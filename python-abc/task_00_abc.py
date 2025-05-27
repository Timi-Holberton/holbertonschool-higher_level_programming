#!/usr/bin/env python3
"""
Définition d'une hiérarchie de classes animales utilisant l'abstraction.

Ce module illustre l'utilisation du module `abc` (Abstract Base Classes)
pour définir une classe abstraite `Animal` avec une méthode abstraite `sound`,
ainsi que deux classes concrètes `Dog` et `Cat` qui implémentent cette méthode
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Classe abstraite représentant un animal.

    Méthodes abstraites :
        sound() : Doit être implémentée par toute sous-classe
        pour définir le cri de l'animal.
    """

    @abstractmethod
    def sound(self):
        """
        Méthode abstraite à implémenter pour produire le son de l'animal.

        Raises:
            NotImplementedError: Si appelée directement sans redéfinition.
        """
        pass


class Dog(Animal):
    """
    Classe représentant un chien, dérivée de Animal.

    Implémente la méthode sound() pour afficher un aboiement.
    """

    def sound(self):
        """
        Affiche le son émis par un chien.
        """
        print("Bark")


class Cat(Animal):
    """
    Classe représentant un chat, dérivée de Animal.

    Implémente la méthode sound() pour afficher un miaulement.
    """

    def sound(self):
        """
        Affiche le son émis par un chat.
        """
        print("Meow")
