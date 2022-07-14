from re import U
import sys
from Fonction import *
from UserClass import User
from BDClass import BD
from LivreClass import Livre
from datetime import timedelta, date
import time

liste_biblio = chargerDonnees()

### DEBUT TEST ###
# Test bibliotheque
# lebook1 = Livre("Force", "le Z", "Français", "comedy", "roman", "ZFORCE4", 1, True, None)
# lebook2 = Livre("Patrie", "La S", "Anglais", "Jeunesse", "roman", "ZFFR544", 3, False, None)
# lebook4 = Livre("Never", "benjy", "Anglais", "Jeunesse", "roman", "ZFYTT8", 2, False, None)
# lebook3 = Livre("Honneur", "le j", "Français", "cpee", "manga", "DTGRCE4", 2, True, None)
# lebook7 = BD("Froid", "le e", "Russe", "cpee", "roman", "DTGRDF4", 2, "Michel", True, True, None)
#
# biblio_a = Bibliotheque("Bibliotheque de Purpan", [], [], [lebook1, lebook2, lebook3, lebook4, lebook7], [])
# biblio_b = Bibliotheque("Bibliotheque de Blagnac", [], [], [], [])
#
# liste_biblio.append(biblio_b)
# liste_biblio.append(biblio_a)

# Personne test
# utilisateur_test = Personne("persoTest", "Corin", "Gaëtan", "Azerty1!")
# utilisateur_test2 = User("Usertest", "Gogulavasan", "Morin-Dietrich", "Admin")
# biblio_a.inscrirePersonne(utilisateur_test)
# biblio_a.inscrirePersonne(utilisateur_test2)
### FIN TEST ###

# Choisir sa bibliothèque (vérifié)
choix_debut = True
while choix_debut:
    for index in range(len(liste_biblio)):
        print(f"{index+1}: {liste_biblio[index].getNom()}")
    print("\n")

    choix_biblio = input("Choisissez votre bibliothèque:\n")
    try:
        choix_biblio = int(choix_biblio)
    except:
        print("Erreur, veuillez réessayer.\n")
    else:
        if int(choix_biblio) <= len(liste_biblio) and int(choix_biblio) > 0:
            choix_debut = False
        else: 
            print("Erreur de saisie, veuillez réessayer.\n")
choix_biblio = choix_biblio -1

BIBLIOTHEQUE_CHOISIE = liste_biblio[choix_biblio]
LES_UTILISATEURS = BIBLIOTHEQUE_CHOISIE.getUtilisateur()

print(f"Vous avez choisi la {BIBLIOTHEQUE_CHOISIE.getNom()}. Bienvenue.")

excecution = True
while excecution:
    test_menu_action = True
    while test_menu_action:
        print("\n")
        choix = input("Choisissez une action:\n 1: Créer un compte\n 2: Se connecter\n 3: Éteindre\n")
        try:
            choix = int(choix)
        except:
            print("Erreur de saisie, veuillez réessayer.")
        else:
            if int(choix) <= 3 and int(choix) > 0:
                test_menu_action = False
            else:
                print("Erreur de saisie, veuillez réessayer.\n")

    # Eteindre (vérifié)
    if choix == 3:
        print("A bientôt.")
        time.sleep(2)
        sauverDonnees(liste_biblio)
        closeProgramme()

    # 1: Créer un compte (vérifié)
    elif choix == 1:
        test_nom = True
        while test_nom:
            futur_nom = input("Entrez votre nom:\n")
            if estEnLettre(futur_nom):
                test_nom = False
            else:
                print("Erreur de saisie, veuillez réessayer.\n")
        nom_valide = False
        while nom_valide == False:
            if verifNom(futur_nom) == True:
                nom_valide = True
            else:
                print("Erreur: Nom invalide, réessayez")
                futur_nom = input("Entrez votre nom:\n")
        prenom_valide = False
        test_prenom = True
        while test_prenom:
            futur_prenom = input("Entrez votre prénom:\n")
            if estEnLettre(futur_prenom):
                test_prenom = False
            else:
                print("Erreur de saisie, veuillez réessayer.\n")
        while prenom_valide == False:
            if verifNom(futur_prenom) == True:
                prenom_valide = True
            else:
                print("Erreur: Prénom invalide, réessayez")
                futur_prenom = input("Entrez votre nom:\n")
        mdp = input("Créez votre mot de passe:\n")
        mdp_valide = False
        while mdp_valide == False:
            if motDePasseValable(mdp) == True:
                mdp_valide = True
            else:
                print("Mot de passe invalide (1 majuscule, 1 minuscule, 1 chiffre, 1 caractère spécial, taille 6 min)\n")
                mdp = input(" votre mot de passe:\n")
        # Corrige la majuscule en début de string (capitalize)
        futur_nom = futur_nom.capitalize()
        futur_prenom = futur_prenom.capitalize()
        futur_ID = utils_genererId(futur_nom, futur_prenom)
        nouveau_personne = Personne(futur_ID, futur_nom, futur_prenom, mdp)
        BIBLIOTHEQUE_CHOISIE.inscrirePersonne(nouveau_personne)
        print(f"Votre ID est:{futur_ID}\nVotre mot de passe est:{mdp}")

    # 2: Se connecter (vérifié)
        # Checker dans la liste des utilisateurs
    elif choix == 2:
        user_connected = None
        while user_connected is None:
            user_id = input("Entrez votre ID:\n")
            user_password = input("Entrez votre mot de passe:\n")
            for une_personne in LES_UTILISATEURS:
                if une_personne.getId() == user_id and une_personne.verifierMotDePasse(user_password):
                    user_connected = une_personne
            if user_connected is None:
                print("\nVotre ID ou votre mot de passe est incorrect ! Veuillez réessayer\n")
            else:
                print("Connexion réussie\n")

    # Le menu avec toutes les fonctionnalités
        retour_menu = True
        while retour_menu:
            print("\n")
            menu_connected = input("Choisissez une action ?\n 1: S'abonner\n 2: Changer son mdp\n 3: Consulter son compte\n 4: Rechercher un livre\n 5: Emprunter un livre\n 6: Rendre un livre\n 7: Prolonger un emprunt\n 8: Afficher les livres disponibles\n 9: Se déconnecter\n\n")

            if menu_connected == "1":
                # 1: S'abonner (vérifié)
                afficherFormules()
                test_formules = True
                while test_formules:
                    choix_formules = input("Choix de votre formule ? (0: Retour)\n")
                    if choix_formules == "0":
                        test_formules = False
                    else:
                        try:
                            choix_formules = int(choix_formules)
                        except:
                            print("Erreur de saisie, veuillez réessayer.\n")
                        else:
                            if int(choix_formules) <= 3 and int(choix_formules) > 0:
                                test_formules = False
                            else:
                                print("Erreur de saisie, veuillez réessayer.\n")

                        formule_choisie = selectionnerFormule(choix_formules)
                        nvo_utilisateur = User(user_connected.getId(), user_connected.getNom(), user_connected.getPrenom(), user_connected.getMdp(), formule_choisie)
                        print(f'\nVous avez choisi la formule: {formule_choisie["Nom formule"]}')
                        # BIBLIOTHEQUE_CHOISIE.supprimerPersonne(user_connected)
                        user_connected = nvo_utilisateur
                        BIBLIOTHEQUE_CHOISIE.inscrirePersonne(user_connected)

            # 2: Changement son mdp (vérifié)
            elif menu_connected =="2":
                new_mdp = False
                while not new_mdp:
                    ancien_mdp = input('Veuillez entrer votre mot de passe actuel: \nmdp:\t')
                    nvo_mdp = input('Veuillez entrer votre nouveau mot de passe : \nmdp:\t')

                    if user_connected.verifierMotDePasse(ancien_mdp) and motDePasseValable(nvo_mdp):
                        user_connected.changerMotDePasse(nvo_mdp)
                        print("Changement de mot de passe réussie !")
                        new_mdp = True
                    else:
                        print("Erreur de saisie, veuillez réessayer.\n")

            # 3: Consulter son compte (vérifié)
            elif menu_connected =="3":
                print("Vos informations personnelles:")
                user_connected.afficherStatutCompte()

            # 4: Rechercher un livre
            elif menu_connected =="4":
                if isinstance(user_connected, User):
                    menu_recherche = True
                    while menu_recherche:
                    # Boucle en cas d'annulation de retour
                        test_menu_recherche = True
                        # test du menu de recherche (vérifié)
                        while test_menu_recherche:
                            ma_recherche = input("Choix de recherche :\n1 : Par mots clés\n2 : Par Auteur\n3 : Par Genre\n4 : Par Catégorie\n5 : Par Langue\n6 : Retour\n ")
                            try:
                                ma_recherche = int(ma_recherche)
                            except:
                                print("\nErreur de saisie, veuillez réessayer.\n")
                            else:
                                if int(ma_recherche) <= 6 and int(ma_recherche) > 0:
                                    test_menu_recherche = False
                                else:
                                    print("\nErreur de saisie, veuillez réessayer.\n")
                        if ma_recherche == 1 :
                            mot_cle = input("Entrez votre mot clé:\n")
                            mot_cle = mot_cle.upper()
                            liste_livre_concernes = BIBLIOTHEQUE_CHOISIE.rechercher(mot_cle)
                            if len(liste_livre_concernes) == 0:
                                print("\nRien ne correspond à votre recherche !\n")
                            else:
                                for i in liste_livre_concernes:
                                    print(i)
                                    menu_recherche = False
                            print("\n")
                        elif ma_recherche == 2 :
                            auteur_livre = input("Le nom de l'auteur ?\n")
                            liste_livre_filtre = BIBLIOTHEQUE_CHOISIE.rechercherAuteur(auteur_livre)
                            if len(liste_livre_filtre) > 0:
                                for livre in liste_livre_filtre:
                                    print(livre)
                                menu_recherche = False
                            else:
                                print("\nRien ne correspond à votre recherche !\n")

                        elif ma_recherche == 3 :
                            genre_livre = input("Quel genre ?\n")
                            liste_livre_filtre = BIBLIOTHEQUE_CHOISIE.rechercherGenre(genre_livre)
                            if len(liste_livre_filtre) > 0:
                                for livre in liste_livre_filtre:
                                    print(livre)
                                menu_recherche = False
                            else:
                                print("\nRien ne correspond à votre recherche !\n")
                        elif ma_recherche == 4 :
                            categorie_livre = input("Quel categorie ?\n")
                            liste_livre_filtre = BIBLIOTHEQUE_CHOISIE.rechercherCategorie(categorie_livre)
                            if len(liste_livre_filtre) > 0:
                                for livre in liste_livre_filtre:
                                    print(livre)
                                menu_recherche = False
                            else:
                                print("\nRien ne correspond à votre recherche !\n")
                        elif ma_recherche == 5 :
                            langue_livre = input("Dans quelle langue ?\n")
                            liste_livre_filtre = BIBLIOTHEQUE_CHOISIE.rechercherLangue(langue_livre)
                            if len(liste_livre_filtre) > 0:
                                for livre in liste_livre_filtre:
                                    print(livre)
                                menu_recherche = False
                            else:
                                print("\nRien ne correspond à votre recherche !\n")
                        elif ma_recherche == 6 :
                            # Test du menu retour (vérifié)
                            test_retour = True
                            while test_retour:
                                retour = input("Etes-vous sûr ?\t 1 : Oui\t2 : Non\n")
                                try:
                                    retour = int(retour)
                                except:
                                    print("\nErreur de saisie, veuillez réessayer.\n")
                                else:
                                    if int(retour) <= 2 and int(retour) > 0:
                                        test_retour = False
                                    else:
                                        print("\nErreur de saisie, veuillez réessayer.\n")
                                if retour == 1:
                                    menu_recherche = False
                                else:
                                    menu_recherche = True
                else:
                    print("\nVous devez être abonné pour accéder à cette fonctionnalité !")

            # 5: Emprunter un livre (vérifié)
            elif menu_connected =="5":
                if isinstance(user_connected, User):
                    menu_recherche = True
                    while menu_recherche:
                        test_menu_recherche = True
                        while test_menu_recherche:
                            mot_recherche = input("Quel livre souhaitez-vous emprunter ?\n")
                            if len(mot_recherche) <= 8 and len(mot_recherche) > 3:
                                    test_menu_recherche = False
                            else:
                                    print("Erreur de saisie, veuillez réessayer.\n")
                                    test_menu_recherche = True
                        BIBLIOTHEQUE_CHOISIE.rechercher(mot_recherche)
                        livre_choisi = BIBLIOTHEQUE_CHOISIE.obtenirLivre(mot_recherche)
                        if livre_choisi == None:
                            print("\nCette référence n'existe pas, veuillez réessayer.\n")
                        else:
                            user_connected.ajouterEmprunt(livre_choisi)
                            taille_livre = livre_choisi.getTaille()
                            end = date.today() + timedelta(days = taille_livre * 7)
                            livre_choisi.emprunter(end)
                            print(f"Le livre que vous avez choisi est:{livre_choisi.getTitre()}\n A rendre avant le:{end}\n")
                            test_menu_recherche = False
                            menu_recherche = False
                else:
                    print("\nVous devez être abonné pour accéder à cette fonctionnalité !")

            # 6: Rendre un livre (vérifié)
            elif menu_connected =="6":
                test_rendre = True
                while test_rendre:
                    if isinstance(user_connected, User):
                        if user_connected.nombreEmpruntEnCours() < 1:
                            print("\nErreur, vous n'avez aucun emprunt actuellement.")
                            test_rendre = False
                        else:
                            print("Vos emprunts:\n")
                            print(user_connected.getEmprunts())
                            rendre_livre = input("Quel livre souhaitez-vous rendre ?\n")
                            livre_choisi = BIBLIOTHEQUE_CHOISIE.obtenirLivre(rendre_livre)
                            user_connected.rendreLivre(livre_choisi)
                            livre_choisi.rendre()
                            print(f"Vous avez rendu:{livre_choisi}\n")
                    else:
                        print("\nVous devez être abonné pour accéder à cette fonctionnalité !")
                        test_rendre = False

            # 7: Prolonger un emprunt (vérifié)
            elif menu_connected =="7":
                test_prolonger = True
                while test_prolonger:
                    if isinstance(user_connected, User):
                        # les_emprunts = user_connected.getEmprunts()
                        if user_connected.nombreEmpruntEnCours() < 1:
                            print("\nErreur, vous n'avez aucun emprunt actuellement.")
                            test_prolonger = False
                        else:
                            print(user_connected.getEmprunts())
                            ref_emprunt = input("Quel est la référence de l'emprunt ?\n")
                            duree_prolongement = int(input("De combien de jours souhaitez-vous prolonger votre emprunt ?\n"))
                            livre_concerne = BIBLIOTHEQUE_CHOISIE.obtenirLivre(ref_emprunt)
                            # Prolonger indisponiblité du livre dans la bibliothèque
                            livre_concerne.prolongerIndisponibilite(duree_prolongement)
                            # Prolonger indisponibilité du livre pour l'utilisateur concerné
                            user_connected.allongerEmprunt(ref_emprunt, duree_prolongement)
                            print(f"L'emprunt a été mis à jour, votre livre {livre_concerne.getTitre()} a bien été prolongé de {duree_prolongement} jours.\n")
                            test_prolonger = False
                    else:
                        print("\nVous devez être abonné pour accéder à cette fonctionnalité !")
                        test_prolonger = False

            # 8: Afficher les livres disponibles (vérifié)
            elif menu_connected =="8":
                test_livre_dispo = True
                while test_livre_dispo:
                    choix= input("\nAfficher:\n \t1: Tout les livre disponibles\n\t2: Livre disponible par Genre\n\t3: Livre disponible par Auteur\n\t4: Livre disponible par Catégorie\n\t5: Livre disponible par Langue\n")
                    try:
                        int(choix) <= 5 and int(choix) > 0
                    except:
                        print("Erreur de saisie, veuillez réessayer.")
                if choix == 1:
                    print("Trier par Disponibilité\n")
                    BIBLIOTHEQUE_CHOISIE.afficherLivreDispo()
                elif choix == 2:
                    print("Trier par Genre\n")
                    BIBLIOTHEQUE_CHOISIE.afficherLivreGenre()
                elif choix == 3:
                    print("Trier par Auteur\n")
                    BIBLIOTHEQUE_CHOISIE.afficherLivreAuteur()
                elif choix == 4:
                    print("Trier par Catégorie\n")
                    BIBLIOTHEQUE_CHOISIE.afficherLivreCategorie()
                elif choix == 5:
                    print("Trier par Langue\n")
                    BIBLIOTHEQUE_CHOISIE.afficherLivreLangue()
                elif choix == 6:
                    test_livre_dispo = False

            # Se deconnecter (vérifié)
            elif menu_connected =="9":
                test_quitter = True
                while test_quitter:
                    quitter = input("Etes-vous sûr de vouloir vous décconecter ?\t 1: Oui     2: Non\n")
                    try:
                        quitter = int(quitter)
                    except:
                        print("Erreur de saisie, veuillez réessayer.")
                    int(quitter) <= 2 and int(quitter) > 0
                    if int(quitter) > 2 or int(quitter) < 0:
                        print("Erreur de saisie, veuillez réessayer.")
                    elif int(quitter) == 1:
                        print("A bientôt.")
                        time.sleep(2)
                        sauverDonnees(liste_biblio)
                        closeProgramme()
                    elif int(quitter) == 2:
                        test_quitter = False

            ### Mode Administrateur ###
            elif menu_connected =="10":
                menu_admin = int(input("Bienvenue dans le menu administrateur, que voulez-faire ?\n\t1: Afficher les livres empruntés\t 2: Afficher les emprunts en retard\t 3: Interface de création\t 4: DEBUG MAX MODE\n"))
                if user_connected.getId() == "Admin":
                    if menu_admin == 1 :
                        livre_admin = BIBLIOTHEQUE_CHOISIE.getListeLivre()
                        for livre in livre_admin:
                            if livre.getDispo() == False:
                                print(livre)
                    elif menu_admin == 2:
                        pass

                    elif menu_admin == 3:
                        print("\n")
                        creation = int(input("Que souhaitez-vous faire ?\n\t1: Créer un livre\t2: Créer une BD\t\t3: Exporter\n"))
                        if creation == 1:
                            print("Veuillez entrez:\n\t\t")
                            nvo_titre = input("\t\tLe titre : ")
                            nvo_auteur = input("\t\tL'auteur : ")
                            nvo_langue = input("\t\tLa langue : ")
                            nvo_genre = input("\t\tLe genre : ")
                            nvo_categorie = input("\t\tLa catégorie : ")
                            nvo_taille = int(input("\t\tLa taille(1, 2, 3,ou 4) : "))
                            nvo_ref = creerRef(nvo_titre,nvo_auteur)
                            nvo_livre = Livre(nvo_titre,nvo_auteur,nvo_langue,nvo_genre,nvo_categorie,nvo_ref,nvo_taille)
                            BIBLIOTHEQUE_CHOISIE.ajouterLivre(nvo_livre)

                        elif creation == 2:
                            print("Veuillez entrez:\n\t\t")
                            nvo_titre = input("\t\tLe titre: ")
                            nvo_auteur = input("\t\tL'auteur: ")
                            nvo_langue = input("\t\tLa langue: ")
                            nvo_genre = input("\t\tLe genre: ")
                            nvo_categorie = input("\t\tLa catégorie: ")
                            nvo_taille = int(input("\t\tLa taille(1, 2, 3 ou 4): "))
                            nvo_dessinateur = input("\t\tLe dessinateur: ")
                            nvo_couleur = input("\t\tEn couleur ?\t Oui / Non")
                            if nvo_couleur.lower() == "oui":
                                nvo_couleur = True
                            else:
                                nvo_couleur = False
                            nvo_ref = creerRef(nvo_titre,nvo_auteur)
                            nvo_livre = BD(nvo_titre,nvo_auteur,nvo_langue,nvo_genre,nvo_categorie,nvo_ref,nvo_taille,nvo_dessinateur,nvo_couleur)
                            BIBLIOTHEQUE_CHOISIE.ajouterLivre(nvo_livre)

                        elif creation == 3:
                            print("save")
                            sauverDonnees(liste_biblio)

                    elif menu_admin == 4:
                        print("\n")
                        debug = int(input("Que souhaitez-vous faire ?\n\t1: Print me\t2: Print users\t3: print this bibliotheque \t4: print book\n"))
                        if debug == 1:
                            print(user_connected.DEBUG_print())
                        if debug == 2:
                            for i in BIBLIOTHEQUE_CHOISIE.getUtilisateur():
                                i.DEBUG_print()
                        if debug == 3:
                            print(BIBLIOTHEQUE_CHOISIE)
                        if debug == 4:
                            print(BIBLIOTHEQUE_CHOISIE.obtenirLivre(input("Entrez la reference : ")))