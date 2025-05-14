#!/usr/bin/python3

def roman_to_int(roman_string):
    # Dictionnaire : chaque chiffre romain a une valeur fixe
    chiffre_romain = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
               'C': 100, 'D': 500, 'M': 1000}

    resultat = 0   # Résultat final à retourner
    precedent = 0    # Dernière valeur lue (initialement 0)

    # On parcourt chaque lettre de la chaîne romaine
    for char in roman_string:
        valeur = chiffre_romain[char]  # On récupère la valeur du symbole

        # Si cette valeur est plus grande que la précédente :
        # exemple : 'IV' (1 avant 5), on fait 5 - 2 * 1 = 3
        if valeur > precedent:
            resultat += valeur - 2 * precedent
        else:
            # Sinon, on ajoute normalement la valeur
            resultat += valeur

        # On garde cette valeur pour la comparer au tour suivant
        precedent = valeur

    # On retourne le nombre entier obtenu
    return resultat
