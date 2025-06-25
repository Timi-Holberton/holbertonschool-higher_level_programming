-- Crée, si elle n'existe pas déjà, une table `id_not_null` avec une colonne `id` entière ayant pour valeur par défaut 1
-- et une colonne `name` contenant une chaîne de caractères.

CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256))
