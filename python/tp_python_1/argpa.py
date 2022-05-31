import argparse
import csv
import os
import re

creafichier = argparse.ArgumentParser()
creafichier.add_argument("-alm", "--addlistmois", type=str, help="crée un dossier liste-mois avec dedans la liste des inscrits, specifier YYYY-MM pour le mois selectionner")
creafichier.add_argument("-pld", "--printlistdivision", type=str, help="print la liste des divisions par ordre decroissante, specifier YYYY-MM pour le mois, ou YYY-MM-JJ pour le jour a lister")
args = creafichier.parse_args()


if args.addlistmois:
    # CREER LE DOSSIER MOIS ET LA LISTE DU MOIS EN UTILISANT LA DONNEE DES LISTES DEJA EXISTANTES
    try:
        os.mkdir("liste_mois")
    except FileExistsError:
        pass

    f = open("liste_mois/inscrits-"+args.addlistmois+".csv", 'w')
    f.close()

    # trouver tous les fichiers voisins et les mets dans une liste
    chemin = os.getcwd()
    liste = (os.listdir(chemin))

    # trouver dans liste les fichiers commencant par args.addlistmois
    for i in liste:
        if re.match("inscrits-"+args.addlistmois, i):
            print(i)
            # ouvrir chaque fichier qui match et afficher chaque ligne
            with open(i, "r") as dossier:
                fichierliste = csv.reader(dossier, delimiter=";")
                for line in fichierliste:
                    print(line)
                    # ouvrir fichier liste-mois, afficher chaque ligne et comparer avec la ligne du fichier qui match /  si pareil, doublon =1
                    doublon = 0
                    csvfile = open("liste_mois/inscrits-"+args.addlistmois+".csv", "r")
                    spamreader = csv.reader(csvfile, delimiter=";")
                    for tuple_total in spamreader:
                        if tuple_total == line:
                            print("doublon-refuser")
                            doublon = 1
                    csvfile.close()
                    # Si aucune ligne identique entre la totalité de liste-mois et la ligne du fichier qui match, alors on ajoute la ligne a liste-mois
                    if doublon != 1:
                        # ajouter la ligne au nouveau fichier créer
                        with open("liste_mois/inscrits-"+args.addlistmois+".csv", 'a', newline='') as csvfile:
                            spamwriter = csv.writer(csvfile, delimiter=';')
                            spamwriter.writerow(line)

if args.printlistdivision:
    # CREER UN FICHIER QUI RASSEMBLE LA DONNEE DE LA PERIODE CIBLER EN UTILISANT LA DONNEE DES LISTES DEJA EXISTANTES

    f = open("printandremove-"+args.printlistdivision+".csv", 'w')
    f.close()

    # trouver tous les fichiers voisins et les mets dans une liste
    chemin = os.getcwd()
    liste = (os.listdir(chemin))

    # trouver dans liste les fichiers commencant par args.printlistdivision
    for i in liste:
        if re.match("inscrits-"+args.printlistdivision, i):
            print(i)
            # ouvrir chaque fichier qui match et afficher chaque ligne
            with open(i, "r") as dossier:
                fichierliste = csv.reader(dossier, delimiter=";")
                for line in fichierliste:
                    print(line)
                    # ouvrir fichier printandremove, afficher chaque ligne et comparer avec la ligne du fichier qui match /  si pareil, doublon =1
                    doublon = 0
                    csvfile = open("printandremove-"+args.printlistdivision+".csv", "r")
                    spamreader = csv.reader(csvfile, delimiter=";")
                    for tuple_total in spamreader:
                        if tuple_total == line:
                            print("doublon-refuser")
                            doublon = 1
                    csvfile.close()
                    # Si aucune ligne identique entre totalité de printandremove et la ligne du fichier qui match, alors on ajoute la ligne a fichier printandremove
                    if doublon != 1:
                        with open("printandremove-"+args.printlistdivision+".csv", 'a', newline='') as csvfile:
                            spamwriter = csv.writer(csvfile, delimiter=';')
                            spamwriter.writerow(line)


    # PRINT LA LISTE printandremove PAR CATEGORIE DE MANIERE DECROISSANT

    classement = [["Non_admis"], ["Poussin"], ["Cadet"], ["Junior"], ["Semi_pro"], ["Pro"]]

    # Recuperer la "categorie" de chaque ligne de printandremove(csv)
    with open("printandremove-"+args.printlistdivision+".csv", "r", newline='') as fichier:
        fieldnames = ['nom', 'prenom', 'email', 'categorie']
        reader = csv.DictReader(fichier, fieldnames=fieldnames, delimiter=';')
        for line in reader:
            # comparer le resultat de line"categorie" avec la liste classement, ajouter donné dans classement si egal
            for i in classement:
                if i[0] == line['categorie']:
                    a = str(line['nom']), str(line['prenom']), str(line['email']), str(line['categorie'])
                    i.append(a)
                else:
                    pass

    # range le tableau categorie du plus remplis en moins remplis
    classement.sort(key=len, reverse=True)

    # print les enregistrement classé par categorie de manière decroissante
    for categorie in classement:
        print("---------")
        for enregistrement in categorie:
            print(enregistrement)

    # supprimer le fichier printandremove
    os.remove("printandremove-"+args.printlistdivision+".csv")

