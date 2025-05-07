#!/usr/bin/python3

# Cette fonction vérifie si le caractère est une minuscule.
# Elle retourne True si c'est une minuscule, False sinon.

def islower(c):
    # Vérifie si le caractère c est une lettre minuscule
    if 97 <= ord(c) <= 122:
        return True  # Minuscule
    else:
        return False  # Pas une minuscule

# même chose mais en une ligne
# def islower(c):
# return 97 <= ord(c) <= 122
