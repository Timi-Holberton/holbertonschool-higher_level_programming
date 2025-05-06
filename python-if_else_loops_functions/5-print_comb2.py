#!/usr/bin/python3

# Boucle de 0 à 99 (range(100) donne 0 à 99 inclus)
for i in range(100):
	# Affiche i sur 2 chiffres
	# Si i != 99 -> on ajoute ", " après
	# Si i == 99 -> on n'ajoute rien après
	print("{:02d}".format(i) if i == 99 else "{:02d}, ".format(i), end="")

# Ajoute un saut de ligne après avoir tout affiché
print()

# -----------------------------------
# Lexique :
# range(100)      -> génère les nombres de 0 à 99
# {:02d}.format(i) -> formate i sur 2 chiffres (0 rempli avec des 0)
# print(..., end=...) -> modifie ce qui est affiché après le print
# i != 99 -> vérifie si i est différent de 99
# i == 99 -> vérifie si i est égal à 99
# print() -> sans argument, fait juste un saut de ligne

# Rappel des notions de base :
# - print() ajoute par défaut un saut de ligne "\n"
# - end permet de changer ce comportement (exemple : end="")
# - format() insère une valeur dans une chaîne en respectant un format
# - range(n) génère une séquence de nombres de 0 à n-1
