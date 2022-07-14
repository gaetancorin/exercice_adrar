import csv

def categorie_age(annee):
    age = 2022 - int(annee)
    if age < 6 or age > 40:
        return "Non_admis"
    elif age < 12:
        return "Poussin"
    elif age < 18:
        return "Cadet"
    elif age < 24:
        return "Junior"
    elif age < 30:
        return "Semi_pro"
    elif age <= 40:
        return "Pro"


def adresse_email(nom,prenom):
    a = str(prenom[0]+"."+nom+"@baton-rouge.fr")
    return a

def ecrire(fichier,liste_final):
    with open(fichier, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';')
        for i in liste_final:
            spamwriter.writerow(i)

def lire(fichier):
    with open(fichier, "r")as f:
        for line in f:
            print(line)
