-- Ce script crée l'utilisateur, s'il n'esxiste ps déjà,
-- lui attribue tous les privilèges sur toutes bases de données,
-- puis applique immédiatement ces droits
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost;
FLUSH PRIVILEGES;
