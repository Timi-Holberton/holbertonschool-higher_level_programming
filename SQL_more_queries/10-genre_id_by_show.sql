-- Cette requête SQL sélectionne le titre des séries (tv_shows.title)
-- ainsi que l’identifiant des genres associés (tv_show_genres.genre_id).
-- Elle effectue une jointure entre les tables tv_shows et tv_show_genres
-- pour ne récupérer que les séries qui ont au moins un genre lié.
-- Les résultats sont triés par ordre alphabétique des titres,
-- puis par ordre croissant des identifiants de genre.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
