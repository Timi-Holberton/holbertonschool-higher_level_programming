#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    # compteur pour suivre combien d'éléments on a réussi à afficher
    nbre_element = 0
    # parcourt les entiers de 0 à x-1 pour afficher jusqu'à x éléments
    for i in range(x):
        try:
            # On tente d'accéder à l'élément d'index i de la liste
            # Si ok, on l'affiche sur la même ligne sans retour à la ligne
            print(my_list[i], end="")
            # Si ok : on incrémente le compteur
            nbre_element += 1

        except IndexError:
            # si l'index i est hors des limites de la liste
            # on sort de la boucle car on ne peut plus rien afficher de plus
            break
# Après avoir terminé l'affichage (ou stop la boucle), on retour à la ligne
    print()
    # On retourne le nombre réel d'éléments affichés avec succès
    return nbre_element
