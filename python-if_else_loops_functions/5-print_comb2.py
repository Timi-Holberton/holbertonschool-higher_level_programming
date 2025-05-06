#!/usr/bin/python3

# Boucle de 0 à 99 (range(100) donne 0 à 99 inclus)
for i in range(100):
    # Affiche i avec 2 chiffres (00 01 02)
    # Si i n'est pas égal à 99, on ajoute ", " après le nombre
    # Si i est égal à 99, on ajoute un saut de ligne "\n"
    print("{:02d}".format(i), end=", " if i != 99 else "\n")

"""
# Lexique :
# range(100)      -> génère les nombres de 0 à 99
# {:02d}.format(i) -> formate i sur 2 chiffres (0 rempli avec des 0)
# print(..., end=...) -> modifie ce qui est affiché après le print
# i != 99 -> vérifie si i est différent de 99
# i == 99 -> vérifie si i est égal à 99

# Rappel des notions de base :
# - print() ajoute par défaut un saut de ligne "\n"
# - end permet de changer ce comportement (exemple : end=", ")
# - format() insère une valeur dans une chaîne en respectant un format
# - range(n) génère une séquence de nombres de 0 à n-1
"""
