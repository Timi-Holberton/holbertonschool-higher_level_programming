#!/usr/bin/python3  # Indique que le script doit être exécuté avec Python 3

# Définition d'une fonction qui met à jour un dictionnaire
def update_dictionary(a_dictionary, key, value):
    # Utilise la méthode .update() pour :
    # - ajouter la paire (key : value) si la clé n'existe pas,
    # - ou modifier la valeur associée à la clé si elle existe déjà
    a_dictionary.update({key : value})

    # Retourne le dictionnaire mis à jour
    return a_dictionary
