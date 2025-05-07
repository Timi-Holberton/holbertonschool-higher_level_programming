#!/usr/bin/python3

# Cette fonction vérifie si le caractère est une minuscule.
# Elle retourne True si c'est une minuscule, False sinon.

def islower(c):
    # Vérifie si le caractère c est une lettre minuscule
    return 97 <= ord(c) <= 122

# Test de la fonction islower avec différents caractères
print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))
