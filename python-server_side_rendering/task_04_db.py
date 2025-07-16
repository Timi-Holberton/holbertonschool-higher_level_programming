from flask import Flask, render_template, request
import json
import csv
import sqlite3

# Création de l'application Flask
app = Flask(__name__)

# ----------- FONCTIONS DE LECTURE DE DONNÉES -----------

def lire_fichier_json(chemin_fichier):
    """Lire les données depuis un fichier JSON et retourner une liste de produits."""
    with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)  # Charge le contenu JSON sous forme de liste de dictionnaires
    return donnees

def lire_fichier_csv(chemin_fichier):
    """Lire les données depuis un fichier CSV et les convertir en liste de dictionnaires."""
    produits = []
    with open(chemin_fichier, encoding='utf-8') as fichier:
        lecteur = csv.DictReader(fichier)  # Lit le CSV sous forme de dictionnaires (ligne par ligne)
        for ligne in lecteur:
            produit = {
                'id': int(ligne['id']),
                'name': ligne['name'],
                'category': ligne['category'],
                'price': float(ligne['price'])
            }
            produits.append(produit)
    return produits

def lire_base_de_donnees_sqlite(nom_fichier_db):
    """Lire les produits depuis une base SQLite et les retourner sous forme de liste de dictionnaires."""
    produits = []
    try:
        # Connexion à la base SQLite
        connexion = sqlite3.connect(nom_fichier_db)
        curseur = connexion.cursor()

        # Requête pour lire tous les produits
        curseur.execute("SELECT id, name, category, price FROM Products")
        lignes = curseur.fetchall()  # Récupère tous les résultats

        # Transformation en liste de dictionnaires
        for ligne in lignes:
            produit = {
                'id': ligne[0],
                'name': ligne[1],
                'category': ligne[2],
                'price': ligne[3]
            }
            produits.append(produit)

        connexion.close()
        return produits

    except sqlite3.Error as erreur:
        # Si une erreur survient dans la base, on lève une exception avec un message personnalisé
        raise RuntimeError(f"Erreur base de données : {erreur}")

# ----------- ROUTE PRINCIPALE -----------

@app.route('/products')
def afficher_produits():
    # Récupère le paramètre 'source' de l'URL : json, csv ou sql
    source = request.args.get('source')

    # Récupère éventuellement un identifiant à filtrer (si présent dans l'URL)
    identifiant = request.args.get('id', type=int)

    # -------- Lecture selon la source choisie --------

    if source == 'json':
        try:
            produits = lire_fichier_json('products.json')
        except Exception:
            return render_template('product_display.html', error="Erreur lecture fichier JSON.")

    elif source == 'csv':
        try:
            produits = lire_fichier_csv('products.csv')
        except Exception:
            return render_template('product_display.html', error="Erreur lecture fichier CSV.")

    elif source == 'sql':
        try:
            produits = lire_base_de_donnees_sqlite('products.db')
        except Exception as erreur:
            return render_template('product_display.html', error=str(erreur))

    else:
        # Si le paramètre 'source' est invalide
        return render_template('product_display.html', error="Wrong source")

    # -------- Filtrage facultatif par identifiant --------

    if identifiant is not None:
        # Filtre la liste des produits pour ne garder que celui dont l'id correspond
        produits_filtres = [produit for produit in produits if produit['id'] == identifiant]

        if not produits_filtres:
            # Si aucun produit ne correspond, affiche un message d'erreur
            return render_template('product_display.html', error="Produit non trouvé.")

        # Sinon, affiche uniquement le produit filtré
        return render_template('product_display.html', products=produits_filtres)

    # Si aucun id n’est spécifié, on affiche tous les produits
    return render_template('product_display.html', products=produits)

# ----------- LANCEMENT DU SERVEUR -----------

if __name__ == '__main__':
    # Démarre le serveur en mode debug (rechargement automatique + erreurs visibles)
    app.run(debug=True)
