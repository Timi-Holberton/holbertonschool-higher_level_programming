-- Crée la table `force_name` avec un entier `id` et un champ texte `name` obligatoire, si elle n'existe pas déjà.
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
