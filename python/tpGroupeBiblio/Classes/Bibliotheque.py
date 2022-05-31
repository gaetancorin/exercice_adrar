from Livre import *
from BD import *
from User import *


class Biblio:

    nomBib = "La petite lecture paisible"

    def __init__(self):
        self.rayon = []
        self.auteur = []
        self.livres = []
        self.utilisateurs = []
        self.categorie = []
        self.langue = []
        self.disponible = []
        self.titre = []

    def __repr__(self):
        return f"{self.rayon},\n{self.auteur},\n{self.utilisateurs},\n{self.categorie},\n{self.langue},\n{self.titre}"

    def importUtilisateurs(self,chemin):
        with open(chemin, "r") as lireUtilisateur:
            for i in lireUtilisateur:
                lesUtilisateurs = i.split(" ; ")
                objUser = User(lesUtilisateurs[0],lesUtilisateurs[1],lesUtilisateurs[2],lesUtilisateurs[3],lesUtilisateurs[5][:-1])
                if len(lesUtilisateurs[4]) == 2:
                    pass
                else:
                    for i in (lesUtilisateurs[4][1:-1].split(", ")):
                        objUser.emprunts.append(i[1:-1])
                self.utilisateurs.append(objUser)

    def exportUtilisateurs(self,chemin):
        with open(chemin, "w") as file:
            for i in self.utilisateurs:
                file.write(str(i)+"\n")

    def importLivres(self,chemin):
        openLivres = open(chemin, "r")
        lireLivres = openLivres.readlines()
        for i in lireLivres:
            lesLivres = i.split(" ; ")
            if len(lesLivres) == 8:
                objLivre = Livre(lesLivres[0],lesLivres[1],lesLivres[2],lesLivres[3],lesLivres[4],lesLivres[5],lesLivres[6],lesLivres[7][:-1])
            else:
                objLivre = BD(lesLivres[0],lesLivres[1],lesLivres[2],lesLivres[3],lesLivres[4],lesLivres[5],lesLivres[6],lesLivres[7],lesLivres[8],lesLivres[9][:-1])
            self.livres.append(objLivre)
            if not objLivre.genre in self.rayon:
                self.rayon.append(objLivre.genre)
            if not objLivre.auteur in self.auteur:
                self.auteur.append(objLivre.auteur)
            if not objLivre.categorie in self.categorie:
                self.categorie.append(objLivre.categorie)
            if not objLivre.langue in self.langue:
                self.langue.append(objLivre.langue)
            if not objLivre.titre in self.titre:
                self.titre.append(objLivre.titre)
            if objLivre.dispo == "True":
                self.disponible.append(objLivre)


    # def ajoutLivre(self):


    def exportLivres(self,chemin):
        with open(chemin, "w") as file:
            for i in self.livres:
                file.write(str(i)+"\n")

    def afficherUtilisateurs(self):
        for i in self.utilisateurs:
            print("id ",i[0],i[1],i[2])

    def triLivres(self, tri):
        for index, i in enumerate(tri):
            print(index+1,": ",i)

    def affichageTri(self,selection,valeur):
        for i in self.disponible:
            if selection == "auteur":
                if i.auteur == self.auteur[valeur]:
                    print(i.titre)
            elif selection == "genre":
                if i.genre == self.rayon[valeur]:
                    print(i.titre)
            elif selection == "categorie":
                if i.categorie == self.categorie[valeur]:
                    print(i.titre)
            elif selection == "langue":
                if i.langue == self.langue[valeur]:
                    print(i.titre)

    def rechercheLivre(self,selection,valeur):
        if selection == "titre":
            for j in self.titre:
                if valeur.lower() in j.lower():
                    print(j)
        if selection == "auteur":
            for j in self.auteur:
                if valeur.lower() in j.lower():
                    print (j)
        if selection == "categorie":
            for j in self.categorie:
                if valeur.lower() in j.lower():
                    print (j)
        if selection == "genre":
            for j in self.rayon:
                if valeur.lower() in j.lower():
                    print (j)

    def ajoutUtilisateur(self,nouvelUtilisateur):
        self.utilisateurs.append(nouvelUtilisateur)
        print("Votre inscription est validée")
