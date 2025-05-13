#!/usr/bin/python3

def max_integer(my_list=[]):
    # Vérifie si la liste est vide
    if my_list == "":
        return None

    # On suppose que le premier élément de la liste est le plus grand
    gros_nombre = my_list[0]

    # Parcours chaque élément de la liste
    for nombre in my_list:
        # Si on trouve un nombre plus grand, on met à jour gros_nombre
        if nombre > gros_nombre:
            gros_nombre = nombre

    # Retourne le plus grand nombre trouvé
    return gros_nombre
