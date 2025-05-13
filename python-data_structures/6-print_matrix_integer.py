#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for ligne in matrix:
        for i in range(len(ligne)):
            if i != len(ligne) - 1:
                print("{:d}".format(ligne[i]), end=" ")
            else:
                print("{:d}".format(ligne[i]), end="")
        print()
