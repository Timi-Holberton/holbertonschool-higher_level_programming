-- Sélectionne l’identifiant et le nom des villes de Californie
-- en filtrant par states.name, sans utiliser JOIN, et trie le résultat par cities.id.
SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id = states.id
AND states.name = 'California'
ORDER BY cities.id ASC;

/*
La requête sélectionne les colonnes `cities.id` et `cities.name`,
c’est-à-dire l’identifiant et le nom des villes.
Les données proviennent des tables `cities` et `states`,
qui sont liées par la condition `cities.state_id = states.id` pour associer
chaque ville à son état correspondant. De plus, un filtre est appliqué pour
ne récupérer que les villes dont l’état est nommé `'California'`.
Enfin, les résultats sont triés par ordre croissant selon l’identifiant
des villes (`cities.id`), permettant d’obtenir une liste ordonnée
des villes californiennes présentes dans la base de données.
*/
