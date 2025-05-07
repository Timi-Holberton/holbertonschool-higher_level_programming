#!/usr/bin/python3

def print_last_digit(number):
    # Calcule la valeur absolue du dernier chiffre
    digit = abs(number) % 10

    # Affiche le dernier chiffre sans saut de ligne
    print(digit, end="")

    # Retourne le dernier chiffre pour pouvoir le réutiliser
    return digit
