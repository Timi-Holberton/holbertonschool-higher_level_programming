#!/usr/bin/python3

def uppercase(str):
    # Chaîne vide qui contiendra le résultat final
    result = ""
    # Parcours chaque caractère de la chaîne donnée en entrée
    for i in str:
        # Si le caractère est une lettre minuscule
        if 97 <= ord(i) <= 122:
            # Convertit le caractère minuscule en majuscule
            result = result + chr(ord(i) - 32)
        else:
            # Si ce n'est pas une minuscule, on garde le caractère inchangé
            result = result + i
    # Affiche la chaîne transformée en majuscules
    print("{}".format(result))
