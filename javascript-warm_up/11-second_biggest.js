#!/usr/bin/node

// Récupère les arguments passés et les convertit en nombres
const arg = process.argv.slice(2).map(Number);

// Si aucun ou un seul argument, on affiche 0
if (arg.length <= 1) {
  console.log(0);
} else {
  // On initialise les deux plus grands nombres avec des valeurs très petites
  let big = Number.NEGATIVE_INFINITY;
  let twoBig = Number.NEGATIVE_INFINITY;

  // Parcours tous les nombres
  for (const nombre of arg) {
    if (nombre > big) {
      // Si le nombre est plus grand que le plus grand actuel,
      // on décale le plus grand vers deuxième plus grand
      twoBig = big;
      big = nombre;
    } else if (nombre > twoBig && nombre < big) {
      // Sinon si le nombre est entre deuxième plus grand et plus grand,
      // on met à jour le deuxième plus grand
      twoBig = nombre;
    }
  }

  // Si deuxième plus grand n'a pas changé, on affiche 0
  if (twoBig === Number.NEGATIVE_INFINITY) {
    console.log(0);
  } else {
    console.log(twoBig);
  }
}
