import csv
import os
import re
# CREER LA LISTE INSCRITS-TOTAL EN UTILISANT LA DONNEE DES LISTES DEJA EXISTANTES

try:
    os.mkdir("inscrits_total")
except FileExistsError:
    pass

# reinitialise inscrits-total
f = open("inscrits_total/inscrits_total.csv", 'w')
f.close()

# trouver tous les fichiers voisins et les mets dans une liste
chemin = os.getcwd()
liste = (os.listdir(chemin))
print(liste)

# trouver dans liste les fichiers commencant par inscrit-20
for i in liste:
    if re.match("inscrits-20", i):
        print(i)
# ouvrir chaque fichier qui match et afficher chaque ligne
        with open(i, "r") as dossier:
            fichierliste = csv.reader(dossier, delimiter=";")
            for line in fichierliste:
                print(line)
# ouvrir fichier inscrit_total, afficher chaque ligne et comparer avec la ligne du fichier qui match /  si pareil, doublon =1
                doublon = 0
                csvfile = open("inscrits_total/inscrits_total.csv", "r")
                spamreader = csv.reader(csvfile, delimiter=";")
                for tuple_total in spamreader:
                    if tuple_total == line:
                        print("doublon-refuser")
                        doublon = 1
                csvfile.close()
# Si aucune ligne identique entre la totalité de inscrit_total et la ligne du fichier qui match, ajouter la ligne a inscrits-total
                if doublon != 1:
                    with open("inscrits_total/inscrits_total.csv", 'a', newline='') as csvfile:
                        spamwriter = csv.writer(csvfile, delimiter=';')
                        spamwriter.writerow(line)


# PRINT LA LISTE INSCRITS-TOTAL PAR CATEGORIE DE MANIERE DECROISSANT

classement = [["Non_admis"], ["Poussin"], ["Cadet"], ["Junior"], ["Semi_pro"], ["Pro"]]

# Recuperer le fieldname categorie de chaque ligne de inscrits-total(csv)
with open("inscrits_total/inscrits_total.csv", "r", newline='') as inscrit_total:
    fieldnames = ['nom', 'prenom', 'email', 'categorie']
    reader = csv.DictReader(inscrit_total, fieldnames=fieldnames, delimiter=';')
    for line in reader:
        # print(line['categorie'])
# comparer le resultat de categorie(du csv) avec la liste classement, ajouter donné dans classement si egal
        for i in classement:
            if i[0] == line['categorie']:
                a = str(line['nom']), str(line['prenom']), str(line['email']), str(line['categorie'])
                i.append(a)
            else:
                pass

# range le tableau categorie du plus remplis en moins remplis
classement.sort(key=len, reverse=True)

# print les enregistrement classé par cotegorie de manière decroissante
for categorie in classement:
    print("---------")
    for enregistrement in categorie:
        print(enregistrement)

