#!/usr/bin/python3

# Affiche l'alphabet en minuscules sauf 'q' et 'e'
for char in range(ord('a'), ord('z') + 1):
    # Parcourt les codes ASCII de 'a' (97) à 'z' (122) inclus

    if char != ord('e') and char != ord('q'):
        # Vérifie que la lettre n'est pas 'e' (101) ni 'q' (113)

        print("{}".format(chr(char)), end="")
        # Affiche le caractère correspondant sans saut de ligne
