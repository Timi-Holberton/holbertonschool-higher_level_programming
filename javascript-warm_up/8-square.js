#!/usr/bin/node

// Convertit le premier argument en entier
const arg = parseInt(process.argv[2]);

// Vérifie si l'argument est un nombre
if (isNaN(arg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg; i++) {
    let row = ''; // Initialise une ligne vide
    // Boucle pour construire une ligne composée de 'X'
    for (let j = 0; j < arg; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
