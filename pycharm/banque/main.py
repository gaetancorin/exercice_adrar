from prenium import Prenium
from user_banque import User
from banque import Banque

BankCorin = Banque()

while True:
    nouveau = input("Vous êtes nouveau? Oui(o) / Non(n)\n")
    if nouveau != "o" and nouveau != "n":
        print("Merci d'inscrire la lettre o ou n\n")

    elif nouveau == "o":
        while True:
            utilisateur = input("Vous souhaiter créer un compte classique(1) ou prenium(2)?ou quitter?(3)\n")
            if utilisateur != "1" and utilisateur != "2" and utilisateur != "3":
                print("Merci d'inscrire le chiffre 1,2 ou 3")
                # SI QUITTER
            elif utilisateur == "3":
                break
                # SI CLASSIQUE
            elif utilisateur == "1":
                enregistrement = User(input("Merci d'inscrire votre Nom de famille\n"), input("Merci d'inscrire votre mot de passe\n"))
                # SI PRENIUM
            elif utilisateur == "2":
                enregistrement = Prenium(input("Merci d'inscrire votre Nom de famille\n"), input("Merci d'inscrire votre mot de passe\n"))

            if utilisateur == "1" or utilisateur == "2":
                enregistrement.afficherInformations()
                print("Nous allons a présent vous créer un compte bancaire chez BankCorin")
                bouleen = 0
                while bouleen == 0:
                    try:
                        somme = int(input("Indiquer la somme que vous souhaiter sur votre compte en premier crédit\n"))
                    except ValueError:
                        print("indiquez la somme en chiffre")
                    else:
                        bouleen = 1
                enregistrement.CreerCompte(somme)

                BankCorin.Ajoutclientetcompte(enregistrement)
                break

    elif nouveau == "n":
        while True:
            print("//////////")
            for i in BankCorin.liste_compteclient:
                print(i.Nom)
            nomdecompte = input("Ecrire votre nom de compte parmis ceux ci-dessus / écrire q pour quitter\n")
            if nomdecompte == "q":
                break
            bouleen = 0
            for i in BankCorin.liste_compteclient:
                if i.Nom == nomdecompte:
                    bouleen += 1
                    motdepasse = input("Ecrire votre mot de passe\n")
                    if i.Mdp != motdepasse:
                        print("Mot de passe incorrect")
                    if i.Mdp == motdepasse:
                        print("Mot de passe correct")
                        while True:
                            if isinstance(i, Prenium):
                                choix = input("Vous souhaiter : Afficher , Debiter, Crediter, Afficher Information, Emprunter, Quitter")
                            else:
                                choix = input(
                                    "Vous souhaiter : Afficher , Debiter, Crediter, Afficher Information, Quitter")

                            if choix == "Afficher":
                                i.CompteBancaire.Afficher()

                            elif choix == "Debiter":
                                bouleen = 0
                                while bouleen == 0:
                                    try:
                                        debiter = int(input("choisir la somme a débiter"))
                                    except ValueError:
                                        print("indiquez la somme en chiffre")
                                    else:
                                        bouleen = 1
                                        i.CompteBancaire.Debiter(debiter)

                            elif choix == "Crediter":
                                bouleen = 0
                                while bouleen == 0:
                                    try:
                                        crediter = int(input("choisir la somme a créditer"))
                                    except ValueError:
                                        print("indiquez la somme en chiffre")
                                    else:
                                        bouleen = 1
                                        i.CompteBancaire.Crediter(crediter)

                            elif choix == "Afficher Information":
                                i.afficherInformations()

                            elif choix == "Emprunter" and isinstance(i, Prenium):
                                bouleen = 0
                                while bouleen == 0:
                                    try:
                                        emprunt = int(input("Quel somme souhaiter vous emprunter?"))
                                    except ValueError:
                                        print("indiquez la somme en chiffre")
                                    else:
                                        bouleen = 1
                                        BankCorin.Emprunter(i, emprunt)
                                        for i in BankCorin.liste_compteclient:
                                            i.CompteBancaire.Afficher()

                            elif choix == "Quitter":
                                break

                            else:
                                print("Inscrire l'action que vous souhaiter effectuer")

            if bouleen == 0:
                print("Aucun compte existant à ce nom")









