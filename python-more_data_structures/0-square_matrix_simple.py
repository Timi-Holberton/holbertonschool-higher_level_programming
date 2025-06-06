#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Pour chaque ligne de la matrice,
    # on applique une fonction qui élève chaque élément au carré
    # puis on convertit le résultat de map() en liste
    matrix2 = [list(map(lambda x: x * x, ligne)) for ligne in matrix]
    return matrix2

# matrix2 =            Nouvelle matrice
# [list(               Convertit l'objet map en une liste itérable
# map(                 Applique une fonction à chaque élément de la ligne
# lambda x: x * x,     Fonction anonyme qui retourne le carré de x (x fois x)
# ligne))              Chaque ligne (liste) de la matrice
# for ligne in matrix] Pour chaque ligne dans la matrice d'origine


#def square_matrix_simple(matrix=[]):
#    grand_stock = []
#    for i in matrix:
#        stock = []
#        for j in i:
#            stock.append(j * j)
#        grand_stock.append(stock)
#    return grand_stock
