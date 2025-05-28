#!/usr/bin/env python3

class VerboseList(list):
    """
    Une sous-classe de la liste Python standard qui affiche un message
    à chaque opération de modification (append, extend, remove, pop).

    Cela peut être utile pour le débogage ou le suivi des modifications
    sur une liste.
    """

    def append(self, item):
        """
        Ajoute un élément à la fin de la liste et affiche un message.

        Args:
            item: L'élément à ajouter.
        """
        super().append(item)
        print(f"Added [{item}] from the list.")

    def extend(self, item):
        """
        Étend la liste avec les éléments d'un itérable et affiche un message.

        Args:
            item: Un itérable contenant les éléments à ajouter.
        """
        super().extend(item)
        print(f"Extended the list with [{len(item)}] items.")

    def remove(self, item):
        """
        Supprime la première occurrence d'un élément de la liste
        et affiche un message.

        Args:
            item: L'élément à supprimer.

        Raises:
            ValueError: Si l'élément n'est pas présent dans la liste.
        """
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, item=-1):
        """
        Supprime et retourne l'élément à l'index spécifié,
        ou le dernier si aucun index n'est donné.
        Affiche un message avec l'élément retiré.

        Args:
            item (int, optional): L'index de l'élément à retirer.
            Par défaut : -1.

        Returns:
            L'élément retiré de la liste.

        Raises:
            IndexError: Si l'index est invalide.
        """
        stock = super().pop(item)
        print(f"Popped [{stock}] from the list.")
        return stock
