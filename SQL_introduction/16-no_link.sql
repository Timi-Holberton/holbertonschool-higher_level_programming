-- Affiche les colonnes `score` et `name` de la table `second_table` pour les lignes où `name` n’est pas NULL, regroupées par score et nom, triées par score décroissant.
SELECT score, name FROM second_table
WHERE name IS NOT NULL
GROUP BY score, name
ORDER BY score DESC;
