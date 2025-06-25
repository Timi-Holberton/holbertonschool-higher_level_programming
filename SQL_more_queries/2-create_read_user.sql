--  Crée une base de données nommée hbtn_0d_2 uniquement si elle n’existe pas déjà.
-- C’est utile pour éviter une erreur si la base a déjà été créée auparavant.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Crée un utilisateur MySQL nommé user_0d_2 qui peut se connecter depuis localhost, avec le mot de passe user_0d_2_pwd.
-- L’option IF NOT EXISTS évite de recréer un utilisateur déjà existant.
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
-- Donne le droit de lecture (SELECT) à l’utilisateur user_0d_2 sur toutes les tables de la base hbtn_0d_2.
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
-- Recharge les droits d’accès pour que les nouvelles permissions soient immédiatement prises en compte par le serveur MySQL.
-- Ce n’est pas toujours obligatoire avec GRANT, mais c’est une bonne pratique pour s'assurer que les modifications sont actives.
FLUSH PRIVILEGES;
