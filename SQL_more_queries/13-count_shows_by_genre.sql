-- Cette requête affiche chaque genre avec le nombre de séries qui lui sont associées.
-- Seuls les genres liés à au moins une série sont affichés, triés par nombre décroissant de séries.
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;

-- Sélectionne le nom du genre et le renomme en genre pour l'affichage et
-- Compte combien de shows sont liés à chaque genre, affiché sous l’alias number_of_shows.
-- Indique que la requête part de la table des genres.
-- Fait une jointure avec la table d’association pour ne garder que les genres liés à au moins un show.
-- Regroupe les résultats par genre afin de permettre le calcul avec COUNT.
-- Trie les genres du plus lié au moins lié, selon le nombre de shows associés.
