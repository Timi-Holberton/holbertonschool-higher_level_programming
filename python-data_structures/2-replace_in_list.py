#!/usr/bin/python3

# Remplacez un élément dans une liste à une position donnée

def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
