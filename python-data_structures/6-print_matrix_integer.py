#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # On prépare deux listes avec deux éléments chacun : on commence avec [0, 0]
    a = [0, 0]
    b = [0, 0]

    # On remplit la liste 'a' avec les éléments de tuple_a s’ils existent
    for i in range(min(2, len(tuple_a))):
        a[i] = tuple_a[i]

    # On remplit la liste 'b' avec les éléments de tuple_b s’ils existent
    for i in range(min(2, len(tuple_b))):
        b[i] = tuple_b[i]

    # On additionne les deux listes élément par élément et on retourne un tuple
    return (a[0] + b[0], a[1] + b[1])
