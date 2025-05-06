#!/usr/bin/python3

# Parcourt les entiers de 97 ('a') à 122 ('z') inclus
for i in range(97, 123):
    # Affiche le caractère correspondant à i sans saut de ligne
    print("{}".format(chr(i)), end="")
