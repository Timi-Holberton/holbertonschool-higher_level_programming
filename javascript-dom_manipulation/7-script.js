fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    const films = data.results;
    const listFilms = document.getElementById('list_movies');
    listFilms.innerHTML = '';

    films.forEach(films => {
      const li = document.createElement('li');
      li.textContent = films.title;
      listFilms.appendChild(li);
    });
  })
  .catch(error => {
    console.error('Erreur lors de la récupération de liste des films', error);
  });

// fetch(...) : envoie une requête HTTP GET à l’API SWAPI pour récupérer la liste des films Star Wars
// .then(response => response.json()) : transforme la réponse brute (format HTTP) en objet JavaScript (format JSON)
// data.results : contient un tableau d’objets, chaque objet représentant un film (avec des propriétés comme title, director, etc.)
// document.getElementById('list_movies') : sélectionne la balise <ul> où afficher les films
// listFilms.innerHTML = '' : nettoie la liste pour éviter les doublons si le script est relancé
// films.forEach(...) : boucle sur chaque film du tableau
// document.createElement('li') : crée un nouvel élément de liste HTML
// li.textContent = films.title : met le nom du film comme texte dans la balise <li>
// listFilms.appendChild(li) : ajoute le <li> dans la <ul> (la liste des films)
// .catch(...) : gère les erreurs possibles (ex. : pas de connexion, réponse invalide, etc.)
