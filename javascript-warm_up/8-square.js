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






/*Write a script that prints a square

-The first argument is the size of the square
-If the first argument can’t be converted to an integer,
 print “Missing size”
-You must use the character X to print the square
-You must use console.log(...) to print all output
-You are not allowed to use var
-You must use a loop (while, for, etc.)

guillaume@ubuntu:~/$ ./8-square.js
Missing size
guillaume@ubuntu:~/$ ./8-square.js School
Missing size
guillaume@ubuntu:~/$ ./8-square.js 2
XX
XX
guillaume@ubuntu:~/$ ./8-square.js 6
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
guillaume@ubuntu:~/$ ./8-square.js -3
guillaume@ubuntu:~/$ */
