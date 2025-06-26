-- Script SQL qui affiche tous les shows avec leurs genres associés.
-- Si un show n'a pas de genre, la colonne du genre affiche NULL.
-- Résultats triés par titre de la série puis nom du genre.
-- Utilise uniquement un SELECT avec des LEFT JOIN pour inclure les shows sans genre.

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;

-- Ce script SQL interroge la base de données hbtn_0d_tvshows pour afficher l'ensemble des séries
-- (tv_shows) ainsi que les genres qui leur sont associés (tv_genres), lorsqu'ils existent.
-- Il utilise des jointures LEFT JOIN afin de conserver tous les shows, y compris ceux qui ne sont
-- liés à aucun genre : dans ce cas, la colonne du genre affichera NULL.
--
-- La requête combine trois tables :
-- - tv_shows : contient la liste des séries télévisées.
-- - tv_show_genres : table de liaison entre les séries et les genres (relation many-to-many).
-- - tv_genres : contient la liste des genres.
--
-- L'affichage comprend deux colonnes : le titre de la série (tv_shows.title) et le nom du genre
-- associé (tv_genres.name). Les résultats sont triés par ordre alphabétique croissant, d'abord
-- sur le titre de la série, puis sur le nom du genre.

