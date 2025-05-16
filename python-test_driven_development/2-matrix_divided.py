#!/usr/bin/python3

def matrix_divided(matrix, div):
    longueur_ligne = len(matrix[0])
    if any(len(ligne) != longueur_ligne for ligne in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    for ligne in matrix:
        for x in ligne:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)"
                                "of integers/floats")
    new_matrix = [[round(x / div, 2) for x in ligne] for ligne in matrix]
    return new_matrix
