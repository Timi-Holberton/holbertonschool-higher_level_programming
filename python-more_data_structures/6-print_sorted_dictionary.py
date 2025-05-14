#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for clé in sorted(a_dictionary):
        print(f"{clé}: {a_dictionary[clé]}")
