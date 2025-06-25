-- Sélectionne l’identifiant et le nom des villes de Californie
-- en filtrant par states.name, sans utiliser JOIN, et trie le résultat par cities.id.
SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id = states.id
AND states.name = 'California'
ORDER BY cities.id ASC;
