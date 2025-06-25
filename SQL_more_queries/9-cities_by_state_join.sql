--
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;

/*
La requête sélectionne trois colonnes : l’identifiant de la ville (`cities.id`),
le nom de la ville (`cities.name`), ainsi que le nom de l’état auquel la ville
appartient (`states.name`). Les données sont extraites des tables `cities` et `states`.
Pour relier ces deux tables, la condition `cities.state_id = states.id` est utilisée,
ce qui garantit que seules les villes associées à leur état correct sont prises en compte.
Enfin, les résultats sont triés par ordre croissant selon l’identifiant
des villes (`cities.id`), ce qui permet d’obtenir une liste ordonnée facilitant
la lecture et l’analyse. Cette requête affiche donc, pour chaque ville de
la base de données, son identifiant, son nom, et le nom de l’état correspondant.
*/
