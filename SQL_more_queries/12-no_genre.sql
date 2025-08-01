-- Cette requête affiche les titres des séries qui n’ont aucun genre associé.
-- Le champ `genre_id` apparaît comme `NULL`, et les résultats sont triés par titre de série.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
