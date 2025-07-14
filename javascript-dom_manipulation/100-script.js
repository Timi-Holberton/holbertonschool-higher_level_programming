document.addEventListener('DOMContentLoaded', function () {
  // Ajoute un nouvel élément <li> "Item" à la liste quand on clique sur #add_item
  document.getElementById('add_item').addEventListener('click', function () {
    const newLi = document.createElement('li');
    newLi.textContent = 'Item';
    document.querySelector('.my_list').appendChild(newLi);
  });

  // Supprime le dernier élément <li> de la liste quand on clique sur #remove_item
  document.getElementById('remove_item').addEventListener('click', function () {
    const removeItem = document.querySelector('.my_list');
    if (removeItem.lastElementChild) {
      removeItem.removeChild(removeItem.lastElementChild);
    }
  });

  // Vide toute la liste quand on clique sur #clear_list
  document.getElementById('clear_list').addEventListener('click', function () {
    const list = document.querySelector('.my_list');
    list.innerHTML = '';
  });
});

// Le script attend que le DOM soit chargé avant d’ajouter les gestionnaires d’événements
// #add_item : au clic, crée un <li> "Item" et l’ajoute à la liste .my_list
// #remove_item : au clic, supprime le dernier <li> si la liste n’est pas vide
// #clear_list : au clic, supprime tous les <li> en vidant le contenu HTML de la liste
