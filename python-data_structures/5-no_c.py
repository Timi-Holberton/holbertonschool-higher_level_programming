#!/usr/bin/python3

def no_c(my_string):
    # Chaine vide qui stockera la nouvelle chaine sans les c et C.
    result = ""

    # On parcourt chaque caractère de my_string
    for caractere in my_string:
        # On vérifie si le caractère n'est ni 'c' ni 'C'
        if caractere != "c" and caractere != "C":
            # Si ce n'est ni 'c' ni 'C', on l'ajoute à la chaîne result
            result += caractere

    # On retourne la nouvelle chaîne qui ne contient plus de 'c' ni de 'C'
    return result
