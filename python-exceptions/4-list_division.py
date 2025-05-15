#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    resultat = []
    # list_length est un nombre qui représente la taille max des listes
    for i in range(list_length):
        try:
            value1 = my_list_1[i]
            value2 = my_list_2[i]
            # variable temporaire qui stock le resultat de la division
            division = value1 / value2

        except ZeroDivisionError: # division par 0
            print("division by 0")
            division = 0

        except TypeError: # ce n'est pas un entier
            print("wrong type")
            division = 0

        except IndexError: # liste plus courte que la limite list_length
            print("out of range")
            # réinitialise division à 0 pour la prochaine boucle
            division = 0

        finally:
            # ajoute le resultat de division -> resultat même si erreur
            resultat.append(division)

    return resultat
