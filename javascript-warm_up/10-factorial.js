#!/usr/bin/node
// Script qui calcule et affiche la factorielle d’un nombre
// Utilise une fonction récursive pour le calcul

// Récupère le premier argument passé en ligne de commande et le convertit en entier
const arg = parseInt(process.argv[2]);

// Fonction récursive qui calcule la factorielle de x
function factorial (x) {
  // Cas de base : si x n'est pas un nombre ou vaut 0, retourne 1 (0! = 1 par définition)
  if (isNaN(x) || x === 0) {
    return 1;
  }
  // Appel récursif : multiplie x par la factorielle de (x-1)
  return x * factorial(x - 1);
}

// Affiche le résultat du calcul de la factorielle de arg
console.log(factorial(arg));
