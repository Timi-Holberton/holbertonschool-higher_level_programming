#!/usr/bin/python3
"""
Ce module contient une fonction pour afficher un texte
avec deux retours à la ligne après chaque '.', '?' ou ':'.
"""

def text_indentation(text):
    """
    Affiche un texte avec deux sauts de ligne après chaque '.', '?' ou ':'.
    Chaque ligne imprimée est nettoyée des espaces en début et fin.

    Args:
        text (str): Le texte à afficher avec indentation.

    Raises:
        TypeError: Si 'text' n'est pas une chaîne de caractères.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    stock_char = ""

    for char in text:
        stock_char = stock_char + char
        if char in ".:?":
            print(stock_char.strip())
            print()
            stock_char = ""

    if stock_char:
        print(stock_char.strip())
