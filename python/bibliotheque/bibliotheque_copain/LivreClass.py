from datetime import timedelta


class Livre:
    
    #taille correspondant à la catégorie de taille, allant de 1 à 4, 1 étant les livres courts, 4 très longs
    def __init__(self, titre, auteur, langue, genre, categorie, ref, taille, disponibilite = True, retour = None):
        self._titre = titre
        self._auteur = auteur
        self._langue = langue
        self._genre = genre
        self._categorie = categorie
        self._ref = ref
        self._taille = taille
        self._dispo = disponibilite
        self._retour = retour
        

    def __repr__(self):
        resultat = f"\tReference: {self._ref}\n\tTitre: {self._titre}\n\tAuteur: {self._auteur}\n\tTaille: {self._taille}\n"
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
    def ligneDeDonnee(self):
        ligne = "False;" + self._titre + ";" + self._auteur + ";" + self._langue + ";" + self._genre + ";" + self._categorie + ";" + self._ref + ";" + str(self._taille) + ";" + str(self._dispo) + ";" + str(self._retour)
        return ligne


    """
    Argument : Aucun
    retour : resultat, string
    description : Retourne une ligne de donnée (sans les booléens) prête à la sauvegarde
    
    """
    def donneeImportante(self):
        resultat = f"{self._titre} {self._auteur} {self._langue} {self._genre} {self._categorie} {self._ref}"
        return resultat.upper()

    
    """
    Argument : nombre_de_jours, integer
    retour : None
    description : prolonge l'indisponibilité d'un livre
    
    """
    def prolongerIndisponibilite(self, nombre_de_jours):
        end = self._retour + timedelta(days=nombre_de_jours)

    
    """
    Argument : date_retour, date
    retour : None
    description : Initialise la date de retour avec celle donnée en entrée
    
    """
    def emprunter(self, date_retour):
        self._dispo = False
        self._retour = date_retour


    """
    Argument : Aucun
    retour : None
    description : Rend un livre disponible et Initialise la date de retour a None
    
    """
    def rendre(self):
        self._dispo = True
        self._retour = None       

    
    def getTitre(self):
        return self._titre
    
    def getAuteur(self):
        return self._auteur
    
    def getLangue(self):
        return self._langue
    
    def getGenre(self):
        return self._genre        
    
    def getCategorie(self):
        return self._categorie
    
    def getReference(self):
        return self._ref
    
    def getTaille(self):
        return self._taille
    
    def getDispo(self):    
        return self._dispo
    
    
    