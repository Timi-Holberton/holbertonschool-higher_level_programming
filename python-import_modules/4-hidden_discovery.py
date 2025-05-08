#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":

	# On crée une boite (liste) avec tous les noms de hidden_4
	boite_a_name = dir(hidden_4)

	# On crée une nouvelle boite triée (liste) contenant
	# seulement les noms sans "__"
	boiteSans__ = sorted(
		# Pour chaque name dans la boite à name
		name for name in boite_a_name
		# On garde le name s'il ne commence pas par "__"
		if not name.startswith("__")
	)

	# On ouvre la boite et on affiche chaque nom dedans
	for name in boiteSans__:
		print(name)
