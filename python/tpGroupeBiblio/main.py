from datetime import *
import sys
sys.path.insert(1, './Classes')
from Classes.Bibliotheque import Biblio,BD,Livre
from Classes.User import User
from art import *
import re

# Rappel : mettre le code suivant dans la console : # python -m ensurepip # python -m pip install art

tprint("Bonjour : )",font="tarty2")
tprint("Bienvenue dans la Bibliotheque",font="tarty2")

bibliotheque = Biblio()
bibliotheque.importUtilisateurs("./References/Utilisateurs.txt")
bibliotheque.importLivres("./References/Livres.txt")

while True:
    connecter = False
    nouveau = input("Souhaitez vous:\n\t"
                    "(1) Vous connecter \n\t"
                    "(2) Vous inscrire \n\t"
                    "(3) Ajouter un livre \n\t"
                    "(4) Quitter\n")
    if nouveau != "1" and nouveau != "2" and nouveau != "3" and nouveau != "4":
        print("Merci d'inscrire le chiffre 1,2,3 ou 4\n")
    elif nouveau == "2": # l'utilisateur n'a pas de compte
        print("Démarrage de votre inscription")
        nom = input("Saisissez votre nom:\n")
        prenom = input("Saisissez votre prénom:\n")
        mdp = input("Saisissez votre mdp:\n")
        grade = input("Combien de livres souhaitez vous emprunter?\n\t"
                      "(1) 1-2 : gratuit\n\t"
                      "(2) 3-4 : 5.00 euros par mois\n\t"
                      "(3) 5-7 : 7.00 euros par mois\n\t"
                      "(4) 7-10 : 9.00 euros par mois\n\t")
        nouvelInscrit = User("",nom, prenom, mdp, grade)
        nouvelInscrit.definirID()
        bibliotheque.ajoutUtilisateur(nouvelInscrit)
        # fonction print le User nouvellement créé
        #  print "Votre inscription est validée"

    elif nouveau == "3":  # Ajouter un livre
        print("Démarrage de l'ajout d'un livre dans la bibliotheque")
        type = input("S'agit-t-il:\n\t"
                     "(1) D'un Roman\n\t"
                     "(2) D'une BD\n\t"
                     "(3) Quitter")
        if type != "1" and type != "2" and type != "3":
            print("Merci d'inscrire le chiffre 1,2, ou 3\n")
        elif type == "1":  # Ajout Roman
            print("Il s'agit un roman")
            categorie = "Roman"
            titre = input("Saisissez le titre:\n")
            auteur = input("Saisissez l'auteur:\n")
            langue = input("Saisissez la langue:\n")
            bibliotheque.triLivres(bibliotheque.rayon)
            choixGenre = input("Choisir un genre, si il n'est pas présent dans les choix, faites 0 \n")
            if choixGenre == "0":
                genre = input("Saisissez le genre de votre roman")
            else:
                genre = bibliotheque.rayon[int(choixGenre) - 1]
            objLivre = Livre(titre,auteur,langue,genre,categorie)
            objLivre.Definirref()
            bibliotheque.ajoutLivre(objLivre)
        elif type == "2": # Ajout BD
            print("Il s'agit d'une BD")
            categorie = "BD"
            titre = input("Saisissez le titre:\n")
            auteur = input("Saisissez l'auteur:\n")
            langue = input("Saisissez la langue:\n")
            bibliotheque.triLivres(bibliotheque.rayon)
            choixGenre = input("Choisir un genre, si il n'est pas présent dans les choix, faites 0 \n")
            if choixGenre == "0":
                genre = input("Saisissez le genre de votre roman")
            else:
                genre = bibliotheque.rayon[int(choixGenre) - 1]
            choixCouleur = input("La BD est-elle colorée:\n\t"
                            "(1) Oui\n\t"
                            "(2) Non")
            if choixCouleur == "1":
                couleur = True
            else:
                couleur = False
            dessinateur = input("Saisissez le nom du dessinateur:\n")
            objBD = BD(titre, auteur, langue, genre, categorie, couleur, dessinateur)
            objBD.Definirref()
            bibliotheque.ajoutLivre(objBD)

    elif nouveau == "1": # l'utilisateur a déjà un compte
        nom = input("Saisissez votre nom:\n")
        prenom = input("Saisissez votre prénom:\n")
        mdp = input("Saisissez votre mdp:\n")
        for i in bibliotheque.utilisateurs:
            if i.nom == nom and i.prenom == prenom and i.mdp == mdp:
                print("Connection réussie")
                connecter = True
                continuer = True
                while continuer:
                    choix = input("Vous désirez :\n\t"
                                  "(1) Changer de mot de passe\n\t"
                                  "(2) Afficher les livres disponibles\n\t"
                                  "(3) Recherche ciblée\n\t"
                                  "(4) Emprunter un livre\n\t"
                                  "(5) Rendre un livre\n\t"
                                  "(6) Prolonger un emprunt\n\t"
                                  "(7) Changer de grade\n\t"
                                  "(8) Se déconnecter\n\t")

                    if choix == "1": # Changer de Mot de Passe
                        i.changerMotDePasse(input("Indiquez votre nouveau mot de passe\n"))

                    elif choix == "2": # Afficher les livres disponibles
                        choix = input("Recherchez :\n\t"
                                      "(1) Par auteur\n\t"
                                      "(2) Par rayon\n\t"
                                      "(3) Par categorie\n\t"
                                      "(4) Par langue\n\t")
                        if choix == "1":
                            bibliotheque.triLivres(bibliotheque.auteur)
                            choix = input("Choisir un auteur\n")
                            if "0" < choix <= str(len(bibliotheque.auteur)):
                                print("Voici les livres disponibles de", bibliotheque.auteur[int(choix) - 1], ":\t")
                                bibliotheque.affichageTri("auteur", int(choix) - 1)
                                input("\nAppuyez sur \"entrer\" pour continuer\n")
                            else:
                                print("Merci d'indiquer un chiffre entre 1 et", str(len(bibliotheque.auteur)))
                        elif choix == "2":
                            bibliotheque.triLivres(bibliotheque.rayon)
                            choix = input("Choisir un genre\n")
                            if "0" < choix <= str(len(bibliotheque.rayon)):
                                print("Voici les livres disponibles du rayon", bibliotheque.rayon[int(choix) - 1], ":\t")
                                bibliotheque.affichageTri("genre", int(choix) - 1)
                                input("\nAppuyez sur \"entrer\" pour continuer\n")
                            else:
                                print("Merci d'indiquer un chiffre entre 1 et", str(len(bibliotheque.rayon)))
                        elif choix == "3":
                            bibliotheque.triLivres(bibliotheque.categorie)
                            choix = input("Choisir une catégorie\n")
                            if "0" < choix <= str(len(bibliotheque.categorie)):
                                print("Voici les livres disponibles de la catégorie", bibliotheque.categorie[int(choix) - 1], ":\t")
                                bibliotheque.affichageTri("categorie", int(choix) - 1)
                                input("\nAppuyez sur \"entrer\" pour continuer\n")
                            else:
                                print("Merci d'indiquer un chiffre entre 1 et", str(len(bibliotheque.categorie)))
                        elif choix == "4":
                            bibliotheque.triLivres(bibliotheque.langue)
                            choix = input("Choisir la langue\n")
                            if "0" < choix <= str(len(bibliotheque.langue)):
                                print("Voici les livres disponibles de la langue", bibliotheque.langue[int(choix) - 1], ":\t")
                                bibliotheque.affichageTri("langue", int(choix) - 1)
                                input("\nAppuyez sur \"entrer\" pour continuer\n")
                            else:
                                print("Merci d'indiquer un chiffre entre 1 et", str(len(bibliotheque.langue)))
                        else:
                            print("Merci d'indiquer un chiffre entre 1 et 4")

                    elif choix == "3":  # Recherche ciblée
                        choix = input("Recherchez :\n\t"
                                      "(1) Par titre\n\t"
                                      "(2) Par auteur\n\t"
                                      "(3) Par categorie\n\t"
                                      "(4) Par genre\n\t")
                        if choix == "1":
                            choix = input(" Quel livre cherchez-vous?\n")
                            # str = choix
                            # if any(re.findall(r'a|b|c', str, re.IGNORECASE)):
                            print(f"Voici les livres comportant {choix} :\t")
                            bibliotheque.rechercheLivre("titre", choix)
                            input("\nAppuyez sur \"entrer\" pour continuer\n")
                            # else:
                            #     print("**********************")
                            #     print("Ce titre n'existe pas !")
                            #     print("**********************")
                            #     input('Taper sur Entrer pour continuer')

                        elif choix == "2":
                            choix = input(" Quel auteur cherchez-vous?\n")
                            print(f"Voici les livres comportant {choix} :\t")
                            bibliotheque.rechercheLivre("auteur", choix)
                            input("\nAppuyez sur \"entrer\" pour continuer\n")
                        elif choix == "3":
                            choix = input(" Quel categorie cherchez-vous?\n")
                            print(f"Voici les livres comportant {choix} :\t")
                            bibliotheque.rechercheLivre("categorie", choix)
                            input("\nAppuyez sur \"entrer\" pour continuer\n")
                        elif choix == "4":
                            choix = input(" Quel genre cherchez-vous?\n")
                            print(f"Voici les livres comportant {choix} :\t")
                            bibliotheque.rechercheLivre("genre", choix)
                            input("\nAppuyez sur \"entrer\" pour continuer\n")
                        else:
                            print("**********************")
                            print("Veuillez faire un choix entre 1 et 4 !")
                            print("**********************")
                            input('Taper sur Entrer pour continuer')

                    elif choix == "4": # Emprunter un livre
                        # enumerer la liste livredisponible et se servir du index pour demander de choisir
                        for index, livreliste in enumerate(bibliotheque.disponible):
                            print("("+str(index+1)+")", livreliste.titre)
                        choixdulivre = int(input("\nQuel livre souhaitez-vous emprunter ? Tapez 0 pour quitter\n"))
                        if choixdulivre != 0:
                            choixdulivre = int(choixdulivre -1)
                            # enumerer la liste livredisponible et ajouter a utilisateur.emprunts si l index correspond a son choix
                            i.emprunts.append(bibliotheque.disponible[choixdulivre].ref)
                            print("\nVous avez emprunté", bibliotheque.disponible[choixdulivre].titre)
                            bibliotheque.disponible.pop(choixdulivre)
                            # enumerer les livres de la bibliotheque et si le titre est identique a celui de la liste emprunt de l'utilisateur, le passer en indisponible avec une date de retour.
                            for livreBiblio in bibliotheque.livres:
                                if livreBiblio.ref == i.emprunts[-1]:
                                    livreBiblio.dispo = "False"
                                    livreBiblio.retour = date.today()+timedelta(days=14)
                                    print("Il faudra rendre le livre avant le", livreBiblio.retour)
                                    # pour pouvoir exporter sans problème : passage du time en string
                                    livreBiblio.retour = str(livreBiblio.retour)
                                    break
                            input('\nTaper sur Entrer pour continuer')


                    elif choix == "5": # Rendre un livre
                        if i.emprunts == []:
                            print("Vous n'avez emprunté aucun livre.")
                            input('\nTaper sur Entrer pour continuer')

                        else:
                            titreLivreEmprunter = {}
                            for index, livreEmprunter in enumerate(i.emprunts):
                                for livreBiblio in bibliotheque.livres:
                                    if livreBiblio.ref == livreEmprunter:
                                        print(("("+str(index+1)+")"), livreBiblio.titre, "// à rendre avant le", livreBiblio.retour)
                                        titreLivreEmprunter[index]=livreBiblio.titre
                            
                            indexLivreARendre = int(input("Quel livre voulais vous rendre?\n"))
                            print("\nLe livre",titreLivreEmprunter[indexLivreARendre-1],"a bien été rendu")
                            #i.emprunts[indexLivreARendre-1].dispo= "True"
                            for livreBiblio in bibliotheque.livres:
                                if livreBiblio.ref == i.emprunts[indexLivreARendre-1]:
                                    livreBiblio.dispo = "True"
                                    livreBiblio.retour = "None"
                                    bibliotheque.disponible.append(livreBiblio)
                            i.emprunts.pop(indexLivreARendre - 1)
                            input('\nTaper sur Entrer pour continuer')

                    elif choix == "6": # Prolonger un Emprunt
                        prolonger = input("Voulez-vous prolonger l'emprunt ? (oui/non)\n")
                        if prolonger.lower() != "non" and prolonger.lower() != "oui":
                            print("Merci d'écrire oui ou non")
                        elif prolonger.lower() == "non":
                            pass
                        else:
                            print("**********************")
                            print("Vos livres en cours sont :\t")
                            print("**********************")
                            decompte = 0
                            titreLivreEmprunter = {}
                            for index,refEmprunter in enumerate(i.emprunts):
                                for stockLivre in bibliotheque.livres:
                                    if refEmprunter == stockLivre.ref:
                                        print("("+str(index+1)+")", "=", stockLivre.titre,"//", "Il doit être rendu d'ici le :", stockLivre.retour)
                                        decompte += 1
                                        livreActuel = {(index+1): stockLivre.titre}
                                        titreLivreEmprunter.update(livreActuel)
                            livre = int(input("Quel livre souhaitez-vous prolonger ?\n"))
                            if livre > decompte or livre < 1:
                                print("Veuillez entrer l'index correspondant à votre livre")
                            else:
                                print(titreLivreEmprunter[livre])
                                duree = input("Combien de temps souhaitez-vous prolonger ? :\n\t"
                                    "(1) 2 semaines\n\t"
                                    "(2) 1 mois\n\t")
                                for stockLivre in bibliotheque.livres:
                                    if titreLivreEmprunter[livre] == stockLivre.titre:
                                        stockLivre.retour = datetime.strptime(stockLivre.retour, "%Y-%m-%d")
                                        # transformation date avec heure en date sans heure
                                        stockLivre.retour = datetime.date(stockLivre.retour)
                                        if duree == "1":
                                            stockLivre.retour = stockLivre.retour + timedelta(days=14)
                                            print("Vous avez jusqu'au", stockLivre.retour, "pour rendre votre livre.")
                                        if duree == "2":
                                            stockLivre.retour = stockLivre.retour + timedelta(days=30)
                                            print("Vous avez jusqu'au", stockLivre.retour, "pour rendre votre livre.")
                                        # pour pouvoir exporter sans problème : passage du time en string
                                        stockLivre.retour = str(stockLivre.retour)
                                print("**********************")

                    elif choix == "7": # Changer de Grade
                        print("**********************")
                        print("Votre grade actuel est :", i.grade)
                        print("**********************")
                        grade = input("Combien de livres souhaitez vous emprunter?\n\t"
                                      "(1) 1-2 : gratuit\n\t"
                                      "(2) 3-4 : 5.00 euros par mois\n\t"
                                      "(3) 5-7 : 7.00 euros par mois\n\t"
                                      "(4) 7-10 : 9.00 euros par mois\n\t")
                        i.ChangerGrade(grade)
                        if "0" < i.grade <= "4":
                            print("**********************")
                            print("Votre nouveau grade est :", i.grade)
                            print("**********************")
                            input('Taper sur Entrer pour continuer')
                        else:
                            print("**********************")
                            print("Veuillez entrer un grade compris entre 1 et 4 !")
                            print("**********************")
                            input('Taper sur Entrer pour continuer')

                    elif choix == "8": # Se Déconnecter
                        continuer = False
                        print("Déconnexion réussie")
                    else:
                        print("Inscrire un chiffre entre 1 et 8")
                break
        if not connecter:
            print("Erreur d'identification")

    elif nouveau == "3": # QUITTER (ça réécrit par-dessus le fichier .txt)
        # tprint("Au revoir : (",font="tarty2")
        bibliotheque.exportUtilisateurs("./References/Utilisateurs.txt")
        bibliotheque.exportLivres("./References/Livres.txt")
        break
