#!/usr/bin/python3
"""
Script de définition de la classe State, liée à la table MySQL 'states'.
"""
# Importe les outils nécessaires pour définir les colonnes d'une table ORM :
# Column permet de déclarer une colonne, Integer pour les entiers,
# String pour les chaînes
from sqlalchemy import Column, Integer, String
# Importe la fonction qui permet de créer une classe de base pour le mappingORM
# Toutes les classes représentant des tables devront hériter de cette base
from sqlalchemy.ext.declarative import declarative_base

# Création de la classe de base pour l'ORM
Base = declarative_base()

# Définition de la classe représentant la table 'states'
class State(Base):
    __tablename__ = "states"  # Nom réel de la table dans MySQL

    # Colonne id : entier, clé primaire, auto-incrémentée, non nulle
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)

    # Colonne name : chaîne de caractères (128), non nulle
    name = Column(String(128), nullable=False)
