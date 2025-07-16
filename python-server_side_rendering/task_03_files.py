from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def lire_fichier_json(chemin_fichier):
    """Lire un fichier JSON et retourner les données."""
    with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)
    return donnees

def lire_fichier_csv(chemin_fichier):
    """Lire un fichier CSV et retourner les produits sous forme de liste de dictionnaires."""
    liste_produits = []

    with open(chemin_fichier, newline='', encoding='utf-8') as fichier:
        lecteur = csv.DictReader(fichier)

        for ligne in lecteur:
            identifiant = int(ligne['id'])
            nom = ligne['name']
            categorie = ligne['category']
            prix = float(ligne['price'])

            produit = {
                'id': identifiant,
                'name': nom,
                'category': categorie,
                'price': prix
            }

            liste_produits.append(produit)

    return liste_produits

@app.route('/products')
def afficher_produits():
    source = request.args.get('source')
    id_filtrer = request.args.get('id', type=int)

    if source == 'json':
        try:
            produits = lire_fichier_json('products.json')
        except Exception:
            return render_template('product_display.html', error="Erreur lors de la lecture du fichier JSON.")

    elif source == 'csv':
        try:
            produits = lire_fichier_csv('products.csv')
        except Exception:
            return render_template('product_display.html', error="Erreur lors de la lecture du fichier CSV.")

    else:
        return render_template('product_display.html', error="Wrong source")

    if id_filtrer is not None:
        produits_filtres = []

        for produit in produits:
            if produit['id'] == id_filtrer:
                produits_filtres.append(produit)

        if not produits_filtres:
            return render_template('product_display.html', error="Product not found")
        return render_template('product_display.html', products=produits_filtres)

    return render_template('product_display.html', products=produits)

if __name__ == '__main__':
    app.run(debug=True)
