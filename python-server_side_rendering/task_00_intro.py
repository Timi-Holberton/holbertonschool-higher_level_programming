#!/usr/bin/python3
from os.path import exists

attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Erreur : le template doit être une chaîne de caractères.")
        return

    if not template.strip():
        print("Le template est vide, aucun fichier de sortie généré.")
        return

    if not isinstance(attendees, list):
        print("Erreur : attendees doit être une liste.")
        return

    if len(attendees) == 0:
        print("Aucune donnée fournie, aucun fichier de sortie généré.")
        return

    for participant in attendees:
        if not isinstance(participant, dict):
            print("Erreur : chaque participant doit être un dictionnaire.")
            return

    for numero_fichier, participant in enumerate(attendees, start=1):
        template_perso = template
        for etiquette in ["name", "event_title", "event_date", "event_location"]:
            valeur_remplace = participant.get(etiquette)
            if valeur_remplace is None:
                valeur_remplace = "N/A"
            template_perso = template_perso.replace(f"{{{etiquette}}}", str(valeur_remplace))

        nom_fichier = f"output_{numero_fichier}.txt"

        if exists(nom_fichier):
            print(f"Attention : le fichier {nom_fichier} existe déjà et va être écrasé.")

        try:
            with open(nom_fichier, "w") as fichier_sortie:
                fichier_sortie.write(template_perso)
        except Exception as erreur:
            print(f"Erreur lors de l’écriture dans {nom_fichier} : {erreur}")
