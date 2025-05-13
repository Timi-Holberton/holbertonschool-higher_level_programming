#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    # Initialise une nouvelle liste qui contiendra True ou False
    vraifaux = []

    # Parcourt chaque élément de la liste d'origine
    for nombre in my_list:
        # Si le nombre est divisible par 2, ajoute True
        if nombre % 2 == 0:
            vraifaux.append(True)
        # Sinon, ajoute False
        else:
            vraifaux.append(False)

    # Retourne la nouvelle liste contenant True ou False
    return vraifaux
