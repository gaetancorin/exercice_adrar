from unittest import result
from LivreClass import Livre

class BD(Livre):

    def __init__(self, titre, auteur, langue, genre, categorie, ref, taille, dessinateur, couleur = True, disponibilite = True, retour = None):
        super().__init__(titre, auteur, langue, genre, categorie, ref, taille, disponibilite, retour)
        self._dessinateur = dessinateur
        self._couleur = couleur
        
        
    def __repr__(self):
        #on utilise pas super() car on veut que la disponibilité (et la date si jamais pas dispo), soit affichée après toutes les infos dans tous les cass
        resultat = f'\tTitre: {self._titre}\n\tAuteur: {self._auteur}\n\tDessinateur: {self._dessinateur}\n\tCouleur: {self._couleur}'
        if self._dispo:
            resultat += "\t--Disponible à l'emprunt--\n"
        else:
            resultat += f"\t--Non disponible avant le: {self._retour}--\n"
        return resultat

    """
    Argument : Aucun
    retour : ligne, string
    description : Retourne une ligne de donnée prête à la sauvegarde
    
    """
    def donneeImportante(self):
        return super().donneeImportante() + f" {self._dessinateur}".upper()


    """
    Argument : Aucun
    retour : resultat, string
    description : Retourne une ligne de donnée (sans les booléens) prête à la sauvegarde
    
    """
    def ligneDeDonnee(self):
        ligne = "True;" + super().ligneDeDonnee()[6:] + ";" + self._dessinateur + ";" + str(self._couleur)
        return ligne