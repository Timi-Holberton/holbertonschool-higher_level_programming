-- Crée la table `unique_id` avec un entier unique par défaut à 1 et un champ texte `name`, si elle n’existe pas déjà.
CREATE TABLE IF NOT EXISTS unique_id (id INT UNIQUE DEFAULT 1, name VARCHAR(256));
