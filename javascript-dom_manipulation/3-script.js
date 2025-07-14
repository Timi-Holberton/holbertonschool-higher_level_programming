
document.getElementById('toggle_header').addEventListener('click', function () {
  const togHeader = document.querySelector('header');

  togHeader.classList.toggle('red');
  togHeader.classList.toggle('green');
});

// Écrivez un script JavaScript qui bascule la classe de l'élément d'en-tête
// lorsque l'utilisateur clique sur la balise id toggle_header :
// L'élément d'en-tête doit toujours avoir une classe : rouge ou verte,
// jamais les deux en même temps et jamais vide. Si la classe actuelle est rouge,
// lorsque l'utilisateur clique sur l'élément id toggle_header,
// la classe doit être mise à jour en verte ; et inversement.
