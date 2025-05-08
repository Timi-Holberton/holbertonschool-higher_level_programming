#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    boiteN = dir(hidden_4)
    boiteSans__ = sorted(name for name in boiteN if not name.startswith("__"))
    for name in boiteSans__:
        print(name)
