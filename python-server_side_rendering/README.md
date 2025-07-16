# 🌐 Flask Server-Side Rendering Project

Ce projet met en œuvre le **Server-Side Rendering (SSR)** avec **Flask** et **Jinja2**. Il permet de générer des pages HTML dynamiques sur le serveur, en utilisant plusieurs sources de données : fichiers JSON, CSV, et une base SQLite.

---

## 🎯 Objectifs pédagogiques

- Comprendre le principe du Server-Side Rendering (SSR) avec Flask
- Manipuler des données depuis plusieurs formats : `JSON`, `CSV`, `SQLite`
- Créer des templates HTML dynamiques avec Jinja2 (boucles, conditions, inclusions)
- Structurer une application web côté serveur
- Gérer les erreurs et les paramètres dans les routes Flask

---

## 🧩 Aperçu des tâches réalisées

| Tâche n° | Fichier Python         | Ce que ça fait                                                                                      | Utilité principale                                                        |
|---------:|------------------------|------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| 0        | `task_00_intro.py`     | Génère des fichiers d'invitation à partir d’un template texte et d’une liste de participants        | Découverte de la logique de substitution de variables dans des templates |
| 1        | `task_01_jinja.py`     | Crée des pages HTML de base avec Jinja (index, about, contact) avec en-têtes et pieds de page       | Premiers pas avec Flask et les inclusions de templates                   |
| 2        | `task_02_logic.py`     | Affiche dynamiquement une liste d’objets lus depuis un fichier JSON avec boucles et conditions      | Gestion de contenu dynamique dans Jinja                                  |
| 3        | `task_03_files.py`     | Lit des fichiers JSON ou CSV pour afficher une liste de produits avec filtre optionnel par ID       | Intégration de sources de données externes dans des templates HTML       |
| 4        | `task_04_db.py`        | Ajoute la lecture des produits depuis une base de données SQLite                                    | Connexion à une base de données et rendu dynamique depuis SQL            |

---

## 🔍 SSR vs CSR – Pourquoi SSR avec Flask ?

| Caractéristique      | SSR (Flask + Jinja)                             | CSR (React, Angular...)                   |
|----------------------|--------------------------------------------------|-------------------------------------------|
| 💡 Rendu initial      | Serveur – HTML complet renvoyé                  | Navigateur – contenu construit via JS     |
| 🔎 SEO                | Excellent – contenu indexable immédiatement     | Moyen – nécessite JS ou prerendering      |
| ⚡ Performance        | Rapide à charger et afficher                    | Plus long au premier chargement           |
| 🔒 Sécurité           | Moins de logique métier exposée au client       | Logique souvent visible en JS             |
| 🛠️ Simplicité        | Parfait pour apps classiques avec peu d'interactions | Idéal pour apps très interactives         |

---
