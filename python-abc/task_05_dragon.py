#!/usr/bin/env python3

"""
Définit des comportements sous forme de mixins et une classe Dragon.

Contenu :
- SwimMixin : ajoute la capacité de nager.
- FlyMixin : ajoute la capacité de voler.
- Dragon : créature mythique combinant les deux capacités et un rugissement.
"""


class SwimMixin:
    """
    Mixin ajoutant la capacité de nager à une classe.

    Méthodes :
        swim() : Affiche que la créature nage.
    """

    def swim(self):
        """
        Affiche un message indiquant que la créature nage.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin ajoutant la capacité de voler à une classe.

    Méthodes :
        fly() : Affiche que la créature vole.
    """

    def fly(self):
        """
        Affiche un message indiquant que la créature vole.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Représente un dragon qui peut nager, voler et rugir.

    Méthodes :
        roar() : Affiche un rugissement.
        swim() : (hérité) Affiche que le dragon nage.
        fly() : (hérité) Affiche que le dragon vole.
    """

    def roar(self):
        """
        Affiche un message représentant le rugissement du dragon.
        """
        print("The dragon roars!")
