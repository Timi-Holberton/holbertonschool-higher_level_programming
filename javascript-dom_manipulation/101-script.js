document.addEventListener('DOMContentLoaded', function () {
  document.getElementById('btn_translate').addEventListener('click', function () {
    const langue = document.getElementById('language_code').value;
    fetch(`https://hellosalut.stefanbohacek.dev/?lang=${langue}`)
      .then(response => response.json())
      .then(data => {
        document.getElementById('hello').textContent = data.hello;
      })
      .catch(error => {
        console.error('Erreur lors de la traduction :', error);
      });
  });
});

// document.addEventListener('DOMContentLoaded', ...) : attend que le DOM soit entièrement chargé avant d’exécuter le script
// document.getElementById('btn_translate').addEventListener('click', ...) : déclenche l'action au clic sur le bouton
// document.getElementById('language_code').value : récupère le code langue sélectionné (ex. "fr", "es", "en")
// fetch(...) : envoie une requête HTTP GET à l’API HelloSalut avec le paramètre de langue
// .then(response => response.json()) : convertit la réponse en JSON
// document.getElementById('hello').textContent = data.hello : insère la traduction dans l’élément HTML avec id "hello"
// .catch(...) : affiche une erreur dans la console si la requête échoue
