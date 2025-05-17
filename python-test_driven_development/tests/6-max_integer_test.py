#!/usr/bin/python3
"""Unittest for max_integer function.
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class Testmax_integer(unittest.TestCase):

    def test_max_au_milieu(self):
        self.assertEqual(max_integer([1, 3, 2]), 3)

    def test_max_en_fin(self):
        self.assertEqual(max_integer([1, 2, 9]), 9)

    def test_max_en_debut(self):
        self.assertEqual(max_integer([9, 1, 2]), 9)

    def test_negatifs(self):
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_un_element(self):
        self.assertEqual(max_integer([42]), 42)

    def test_liste_vide(self):
        self.assertIsNone(max_integer([]))

    def test_chaine(self):
        self.assertEqual(max_integer("abc"), "c")

    def test_liste_de_chaines(self):
        self.assertEqual(max_integer(["abc", "xyz", "def"]), "xyz")

if __name__ == '__main__':
    unittest.main()
