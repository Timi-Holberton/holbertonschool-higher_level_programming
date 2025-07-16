import sqlite3

def creer_base_de_donnees():
    connexion = sqlite3.connect('products.db')
    curseur = connexion.cursor()

    # Création de la table si elle n'existe pas
    curseur.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    # Insertion de données d'exemple
    curseur.execute('''
        INSERT OR REPLACE INTO Products (id, name, category, price)
        VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')

    connexion.commit()
    connexion.close()

if __name__ == '__main__':
    creer_base_de_donnees()
