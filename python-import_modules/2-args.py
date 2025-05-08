#!/usr/bin/python3

# Importation du module sys qui permet d'accéder aux paramètres
# passés en ligne de commande dans sys.argv
import sys

# Vérifie si aucun argument n'est passé en ligne de commande
# sys.argv contient toujours au moins un élément : le nom du script
if len(sys.argv) == 1:
    # Si la longueur est 1, cela signifie qu'aucun argument
    print("0 arguments.")

else:
    # Si au moins 1 argument, on affiche le nombre total d'arguments
    # (en soustrayant 1 car on ne compte pas le nom du script lui-même)
    print("{} arguments:".format(len(sys.argv) - 1))
    for i in range(1, len(sys.argv)):
        # La boucle for commence à 1 car on saute sys.argv[0] (nom du script)
        # On parcourt tous les arguments donnés par l'utilisateur
        # À chaque itération, i est l'index de l'argument
        # sys.argv[i] est la valeur de l'argument à cet index
        print("{}: {}".format(i, sys.argv[i]))
