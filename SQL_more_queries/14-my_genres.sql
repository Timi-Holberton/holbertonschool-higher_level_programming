-- Cette requête affiche les noms des genres associés à la série "Dexter".
-- Elle relie les tables tv_shows, tv_show_genres et tv_genres pour récupérer
-- les genres liés à la série, filtre sur le titre 'Dexter',
-- puis trie les résultats par ordre alphabétique des genres.

SELECT tv_genres.name
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;

/*
Cette requête a pour objectif d’afficher tous les genres associés à la série "Dexter".
Elle commence par sélectionner les noms des genres depuis la table tv_genres.
Pour y parvenir, elle effectue d’abord une jointure interne (INNER JOIN)
entre tv_shows et tv_show_genres en liant les identifiants des séries (tv_shows.id)
avec les identifiants de shows présents dans la table d’association (tv_show_genres.show_id).
Cette jointure permet de récupérer tous les genres associés à chaque série.

Ensuite, une deuxième jointure interne est effectuée avec la table tv_genres,
en associant chaque genre_id de la table de liaison (tv_show_genres) à l’identifiant
réel du genre dans tv_genres. Cela permet d’obtenir le nom lisible du genre au lieu
de son identifiant.

La clause WHERE tv_shows.title = 'Dexter' limite les résultats à la série portant ce titre,
ce qui signifie que seuls les genres associés à Dexter seront affichés.
Enfin, la clause ORDER BY tv_genres.name ASC trie ces genres par ordre alphabétique
croissant, rendant l’affichage plus lisible.

En résumé, cette requête explore la relation many-to-many entre les séries et les genres,
et filtre précisément sur une série donnée pour en lister tous les genres associés de
manière ordonnée.
*/
