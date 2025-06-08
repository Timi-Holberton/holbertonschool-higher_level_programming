#!/usr/bin/python3
"""
Génère un triangle de Pascal
"""


def pascal_triangle(n):
    """
    Génère le triangle de Pascal jusqu'à la n-ième ligne.

    Chaque ligne du triangle commence et finit par 1. Les éléments
    intermédiaires sont obtenus en sommant deux éléments adjacents de la
    ligne précédente.

    Args:
        n (int): Nombre de lignes du triangle à générer. Doit être >= 0.

    Returns:
        list[list[int]]: Liste de listes, chaque sous-liste représentant une
                         ligne du triangle de Pascal.

    Exemple:
        pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """

    if n <= 0:
        return []  # Retourne liste vide si n <= 0

    liste = [[1]]  # Initialisation avec la première ligne du triangle

    for i in range(1, n):  # crée une séquence de nombres entiers de 1 à n-1
        ligne_precedent = liste[i - 1]  # Récupère la ligne précédente
        new_ligne = [1]  # Débute la nouvelle ligne par 1

        # On boucle jusqu'à len(ligne_precedent) - 1 pour éviter d'accéder
        # à un indice hors limite lors de l'accès à ligne_precedent[j + 1],
        # car j+1 doit rester un indice valide.
        for j in range(len(ligne_precedent) - 1):
            # Ajoute le result des 2 nombres adjacents de la ligne précédente
            new_ligne.append(ligne_precedent[j] + ligne_precedent[j + 1])

        new_ligne.append(1)  # Termine la nouvelle ligne par 1
        liste.append(new_ligne)  # Ajoute la nouvelle ligne au triangle
    return liste  # Retourne la liste complète représentant le triangle
