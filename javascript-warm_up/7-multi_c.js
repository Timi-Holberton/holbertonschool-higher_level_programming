#!/usr/bin/node

// Affiche un certain nombre de fois en fonction
// de la donnée passé en argument

const x = parseInt(process.argv[2]);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
