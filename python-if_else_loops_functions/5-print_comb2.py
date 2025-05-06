#!/usr/bin/python3

# Boucle de 0 à 99 (range(100) donne 0 à 99 inclus)
for i in range(100):
	# Affiche i avec 2 chiffres (00 01 02)
	# Si i n'est pas égal à 99, on ajoute ", " après le nombre
	# Si i est égal à 99, on ajoute un saut de ligne "\n"
	print("{:02d}".format(i), end=", " if i != 99 else "\n")
