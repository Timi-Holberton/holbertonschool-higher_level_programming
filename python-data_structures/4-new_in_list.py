#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        copy1 = my_list.copy()
        return copy1
    else:
        copy2 = my_list.copy()
        copy2[idx] = element
        return copy2
