#!/usr/bin/python3

# Définition de la fonction qui prend deux ensembles (set_1 et set_2)
def common_elements(set_1, set_2):
    # Utilisation de l'opérateur & pour trouver les éléments communs aux 2
    resultat = set_1 & set_2
    # Retourne le résultat, les éléments communs
    return resultat
