from premium import *
from banque import *
monUser = User("harry","Azerty77")
info_user = [monUser]

while True :
    demande = input("Etes vous nouveau ?\n(o/n)\n")


    if demande == "o":
        
        choix = int(input("\nVoulez-vous:\n\tCreer un compte utilisateur: Entrez 1\n\tCreer un compte Premium: Entrez 2\n"))

        nom = input("Entrez votre nom\n")
        mdp = input("Entrez votre mot de passe\n")

        if choix == 1:
            mon_user = User(nom,mdp)
            info_user.append(mon_user)
            
            for i in info_user:
                print(f"\tBonjour, {i} votre compte utilisateur a bien été creé !\n")
            mon_user.CreerCompte(int(input("Veuillez entrez le montant initial a deposé !\n")))
            while True:
                decision = int(input("Que voulez vous faire ?\n\t"
                                "1: Visualiser votre solde\n\t"
                                "2: créditer votre compte\n\t"
                                "3: débiter votre compte\n\t"
                                "4: Afficher vos crédits éffectués\n"
                                "5: Quitter\n"))
                if decision == 1:
                    mon_user.compte_bancaire.Afficher()
                elif decision == 2:
                    montant = int(input("de combien souhaitez vous créditer ?\n"))
                    mon_user.compte_bancaire.Crediter(montant)
                elif decision == 3:
                    mont= int(input("de combien souhaitez vous débiter ?\n"))
                    mon_user.compte_bancaire.Debiter(mont)
                elif decision == 4:
                    mon_user.compte_bancaire.AfficherCredits()
                else:
                    print("Au revoir")
                    break

        elif choix == 2 :
            mon_user = Premium(nom,mdp)
            info_user.append(mon_user)
            for i in info_user:
                print(f"\tBonjour, {i} votre compte utilisateur a bien été creé !\n")
            mon_user.CreerCompte(int(input("Veuillez entrez le montant initial a deposé !\n")))
            while True:
                decision = int(input("Que voulez vous faire ?\n\t"
                                "1: Visualiser votre solde\n\t"
                                "2: Créditer votre compte\n\t"
                                "3: Débiter votre compte\n\t"
                                "4: Afficher vos crédits éffectués\n"
                                "5: Effectuer un emprunt\n"
                                "6: Quitter\n"))
                if decision == 1:
                    mon_user.compte_bancaire.Afficher()
                elif decision == 2:
                    montant = int(input("de combien souhaitez vous créditer ?\n"))
                    mon_user.compte_bancaire.Crediter(montant)
                elif decision == 3:
                    mont= int(input("de combien souhaitez vous débiter ?\n"))
                    mon_user.compte_bancaire.Debiter(mont)
                elif decision == 4:
                    mon_user.compte_bancaire.AfficherCredits()
                elif decision == 5:
                    emprunt = int(input("combien voulez-vous emprunter\n"))
                    mon_user.Emprunter(emprunt)
                    
                    
                    
                else:
                    print("Au revoir")
                    break

    
    else :
        nom = input("Veuiilez entrez votre nom d'utilisateur\n")
        mdp = input("Veuillez entrez le mot de passe de votre compte utilisateur\n")
        for i in info_user:
            if i.nom == nom and i.mdp == mdp:
                if isinstance(i, Premium):
                    while True:
                        decision = int(input("Que voulez vous faire ?\n\t"
                                        "1: Visualiser votre solde\n\t"
                                        "2: Créditer votre compte\n\t"
                                        "3: Débiter votre compte\n\t"
                                        "4: Afficher vos crédits éffectués\n"
                                        "5: Effectuer un emprunt\n"
                                        "6: Quitter\n"))
                        if decision == 1:
                            mon_user.compte_bancaire.Afficher()
                        elif decision == 2:
                            montant = int(input("de combien souhaitez vous créditer ?\n"))
                            mon_user.compte_bancaire.Crediter(montant)
                        elif decision == 3:
                            mont= int(input("de combien souhaitez vous débiter ?\n"))
                            mon_user.compte_bancaire.Debiter(mont)
                        elif decision == 4:
                            mon_user.compte_bancaire.AfficherCredits()
                        elif decision == 5:
                            emprunt = int(input("combien voulez-vous emprunter\n"))
                            mon_user.Emprunter(emprunt)
                        else:
                            print("Au revoir")
                            break
                else:
                    while True:
                        decision = int(input("Que voulez vous faire ?\n\t"
                                        "1: Visualiser votre solde\n\t"
                                        "2: Créditer votre compte\n\t"
                                        "3: Débiter votre compte\n\t"
                                        "4: Afficher vos crédits éffectués\n"
                                        "5: Quitter\n"))
                        if decision == 1:
                            mon_user.compte_bancaire.Afficher()
                        elif decision == 2:
                            montant = int(input("de combien souhaitez vous créditer ?\n"))
                            mon_user.compte_bancaire.Crediter(montant)
                        elif decision == 3:
                            mont= int(input("de combien souhaitez vous débiter ?\n"))
                            mon_user.compte_bancaire.Debiter(mont)
                        elif decision == 4:
                            mon_user.compte_bancaire.AfficherCredits()
                        else:
                            print("Au revoir")
                            break
            else :
                print("Vous n'avez pas de compte utilisateur\n")            