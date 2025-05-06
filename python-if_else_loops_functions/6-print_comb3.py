#!/usr/bin/python3

for i in range(10):
    for j in range(i + 1, 10):
# Affiche les combinaisons avec virgule et 1 espace, sauf pour la dernière
        if i == 8 and j == 9:
            print("{}{}".format(i, j))  # Dernière combinaison sans virgule
        else:
            print("{}{}".format(i, j), end=", ")
