-- Affiche les colonnes `score` et `name` de la table `second_table` pour les scores supérieurs ou égaux à 10, triées par score décroissant.
SELECT score, name FROM second_table WHERE score >= 10
ORDER BY score DESC;
