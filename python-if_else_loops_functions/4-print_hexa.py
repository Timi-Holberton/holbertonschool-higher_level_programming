#!/usr/bin/env python3

# Programme qui affiche les nombres de 0 à 98 en décimal et hexadécimal

# Boucle qui parcourt les entiers de 0 à 98 inclus
for i in range(99):
    # Affiche le nombre i en deux formats :
    # - {} affiche i en décimal (base 10)
    # - {:x} affiche i en hexadécimal (base 16, minuscules)
    # La chaîne obtenue est de la forme "i = 0xHEX"
    # Par exemple, pour i = 10 -> "10 = 0xa"
    print("{} = 0x{:x}".format(i, i))
