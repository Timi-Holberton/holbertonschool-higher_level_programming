#!/usr/bin/python3  # Indique que ce script doit être exécuté avec Python 3

# Définition de la fonction best_score qui prend un dictionnaire en argument
def best_score(a_dictionary):
    # Si le dictionnaire est vide ou None, on retourne None
    if not a_dictionary:
        return None
    else:
        # Sinon, on retourne la clé dont la valeur est la plus élevée
        # max() parcourt les clés,
        # mais key=a_dictionary.get indique de comparer selon les valeurs
        return max(a_dictionary, key=a_dictionary.get)
