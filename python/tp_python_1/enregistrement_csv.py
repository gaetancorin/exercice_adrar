from datetime import date
import csv

# a = str(date.today())
# print("inscrits-"+ a)
#
# liste_final = [['corin', 'gaetan', 'g.corin@baton-rouge.fr', 'Semi-pro'], ['jaquie', 'michel', 'm.jaquie@baton-rouge.fr', 'Junior'], ['antoine', 'daniel', 'd.antoine@baton-rouge.fr', 'Cadet']]

def ecrire(fichier,liste_final):
    with open(fichier, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';')
        for i in liste_final:
            spamwriter.writerow(i)

def lire(fichier):
    with open(fichier, "r")as f:
        for line in f:
            print(line)

# ecrire("inscrits-"+ a+".csv", liste_final)
# lire("inscrits-"+ a+".csv")
