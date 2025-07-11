#!/usr/bin/node

// Fonction add qui retourne la somme de deux entiers a et b
function add(a, b) {
  return a + b;
}

// Rend la fonction visible à l'extérieur du module
module.exports = {
  add
};
