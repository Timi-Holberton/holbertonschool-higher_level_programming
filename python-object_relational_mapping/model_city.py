#!/usr/bin/python3
"""
Définition de la classe City, liée à la table MySQL 'cities',
représentant les villes, avec SQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.schema import ForeignKey
from model_state import Base
from sqlalchemy.orm import relationship

class City(Base):
    """
    Classe City mappée à la table 'cities' de la base de données.

    Attributs :
    id (int) : identifiant unique de la ville, clé primaire, auto-incrémentée.
    name (str) : nom de la ville, chaîne de 128 caractères max, non nulle.
    state_id (int) : identifiant de l'état auquel appartient la ville,
                         clé étrangère vers 'states.id', non nul.
    """
    __tablename__ = 'cities'  # Nom réel de la table dans MySQL

    # Colonne 'id' : entier, clé primaire, auto-incrémentée, non nulle
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    # Colonne 'name' : nom de la ville, non nul, chaîne max 128 caractères
    name = Column(String(128), nullable=False)

    # Colonne 'state_id' : clé étrangère vers 'states.id', non nulle
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State")
