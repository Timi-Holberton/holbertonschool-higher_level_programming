-- Cette requête extrait les titres de toutes les séries liées au genre "Comedy".
-- Elle utilise des jointures entre les tables tv_shows, tv_show_genres et tv_genres
-- pour relier chaque série à ses genres correspondants.
-- Ensuite, elle filtre les résultats pour ne garder que celles dont le genre est "Comedy",
-- puis trie les titres obtenus par ordre alphabétique croissant.

SELECT tv_shows.title
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = "Comedy"
ORDER BY tv_shows.title ASC;
