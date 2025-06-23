-- Compte le nombre d’enregistrements par score dans `second_table` et affiche les scores avec leur nombre triés par nombre décroissant.
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
