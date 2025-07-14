fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    document.getElementById('character').textContent = data.name;
  })
  .catch(error => {
    console.error('Erreur lors de la récupération du personnage :', error);
  });

// fetch(...) envoie une requête HTTP GET à l'URL de l'API Star Wars pour obtenir les données du personnage n°5
// .then(response => response.json()) Quand la réponse arrive, on la convertit en JSON (objet JavaScript)
// .then(data => { Une fois les données JSON obtenues, on les utilise
// .then(data => { ... }) On insère le nom du personnage dans l'élément HTML qui a l'id 'character'
// .catch(...) Si une erreur se produit pendant la requête ou le traitement, on l'affiche dans la console
