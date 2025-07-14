
document.getElementById('add_item').addEventListener('click', function () {
  const newLi = document.createElement('li');
  newLi.textContent = 'Item';
  document.querySelector('.my_list').appendChild(newLi);
});

// Quand l'utilisateur clique sur l'élément avec l'id 'add_item'
// On crée un nouvel élément <li>
// On définit le texte à l'intérieur du <li>
// On ajoute ce <li> à la <ul> qui a la classe 'my_list'
