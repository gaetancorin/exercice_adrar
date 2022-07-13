from libmoi import *
from datetime import date

nom = (input("Entrez le nom de la personne\n"))
prenom = (input("Entrez le prénom de la personne\n"))
annee = int(input("Entrez l'année de naissance de la personne\n"))


a = Mail(nom, prenom) 
b = Categorie((2022-annee))

print(f"Nom: {nom}\nPrénom: {prenom}\nMail: {a}\nCatégorie: {b}\n")
