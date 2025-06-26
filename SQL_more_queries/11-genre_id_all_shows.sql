-- Cette requête affiche la liste de toutes les séries, ainsi que l’identifiant
-- de leur genre s’il existe. Les séries sans genre apparaissent quand même,
-- avec une valeur `NULL`. Les résultats sont triés par titre de série
-- et identifiant de genre.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
