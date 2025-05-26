#!/usr/bin/python3
"""Classe héritée de list
"""


class MyList(list):
    """Classe héritée de list, avec une méthode pour afficher la liste triée.
    """
    def print_sorted(self):
        """Affiche la liste triée en ordre croissant sans la modifier.
        """
        print(sorted(self))
