#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    # Vérifie si l'index est valide : il doit être >= 0 et < taille de la liste
    if idx >= 0 and idx < len(my_list):
        # Supprime l'élément à la position idx
        del my_list[idx]
        # Retourne la liste modifiée
        return my_list

    # Si l'index est invalide, retourne la liste d'origine inchangée
    return my_list
