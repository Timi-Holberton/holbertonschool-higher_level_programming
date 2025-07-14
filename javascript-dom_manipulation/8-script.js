document.addEventListener('DOMContentLoaded', function () {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(data => {
      document.getElementById('hello').textContent = data.hello;
    });
});

// document.addEventListener('DOMContentLoaded', ...) : attend que tout le HTML soit chargé avant d'exécuter le script
// fetch(...) : envoie une requête HTTP GET à l'API pour obtenir la traduction du mot "hello" en français
// .then(response => response.json()) : convertit la réponse brute en objet JavaScript (JSON)
// .then(data => { ... }) : extrait la valeur de la propriété "hello" contenue dans l'objet JSON
// document.getElementById('hello').textContent = data.hello : insère le mot traduit dans l'élément HTML avec id="hello"
