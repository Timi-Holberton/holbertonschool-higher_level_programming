#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
        boite_a_name = dir(hidden_4)
        boiteSans__ = sorted(name for name in boite_a_name if not name.startswith("__"))
	for name in boiteSans__:
		print(name)
