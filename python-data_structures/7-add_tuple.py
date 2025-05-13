#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # On tronque ou complète les tuples à 2 éléments
    tuple_a = tuple_a[:2] + (0, 0)
    tuple_b = tuple_b[:2] + (0, 0)

    # Addition des deux premiers éléments
    resultat = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return resultat
