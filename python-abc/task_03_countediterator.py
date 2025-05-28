#!/usr/bin/env python3

class CountedIterator:
    """
    Un itérateur qui compte le nombre d'éléments extraits.

    Cette classe encapsule un itérable et permet de suivre combien d'éléments
    ont été récupérés lors de l'itération.

    Attributes:
        iterator (iterator): L'itérateur sous-jacent créé
        à partir de l'itérable donné.
        count (int): Le nombre d'éléments déjà extraits via `__next__()`.
    """

    def __init__(self, __iter__):
        """
        Initialise le CountedIterator avec un itérable.

        Args:
            __iter__ (iterable): Un objet itérable à encapsuler.
        """
        self.iterator = iter(__iter__)
        self.count = 0

    def __iter__(self):
        """
        Retourne l'objet lui-même comme itérateur.

        Returns:
            CountedIterator: L'instance actuelle de l'itérateur.
        """
        return self

    def get_count(self):
        """
        Retourne le nombre d'éléments déjà extraits.

        Returns:
            int: Le nombre d'appels à `__next__()` réussis.
        """
        return self.count

    def __next__(self):
        """
        Retourne l'élément suivant de l'itérateur,
        en incrémentant le compteur.

        Returns:
            Any: L'élément suivant de l'itérable sous-jacent.

        Raises:
            StopIteration: Si l'itérable sous-jacent est épuisé.
        """
        element = next(self.iterator)
        self.count += 1
        return element
