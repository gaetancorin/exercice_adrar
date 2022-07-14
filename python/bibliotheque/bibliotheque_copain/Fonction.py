from BibliothequeClass import Bibliotheque
from LivreClass import Livre
from BDClass import BD
from PersonneClass import Personne
from UserClass import User
import os
import Rules
from os import system, name
import datetime
import random



"""
    Argument : Aucun
    retour : list<bibliotheque>
    description :-permet de lire les données des fichiers
                 -retourn une liste d'objet bibliothèque

"""
def chargerDonnees():
    f = open("liste_bibliotheque.txt", "r")
    liste_de_bibliotheque = []
    for biblio_line in f:
        biblio = biblio_line[:-1]
        # creation de la bibliotheque
        une_bibliotheque = Bibliotheque(biblio)

        # ouverture des fichiers liés à la bibliotheque


        fichier_rayon = open(f"biblio_{une_bibliotheque.getNom()}_rayons.txt")
        fichier_auteurs = open(f"biblio_{une_bibliotheque.getNom()}_auteurs.txt")
        fichier_livres = open(f"biblio_{une_bibliotheque.getNom()}_livres.txt")
        fichier_utilisateurs = open(f"biblio_{une_bibliotheque.getNom()}_utilisateurs.txt")

        # initialisation des futures données de la bibliotheque
        liste_rayons = []
        liste_auteurs = []
        liste_livres = []
        liste_utilisateurs = []

        # lectures des fichiers, ajouts dans les listes
        for ligne_rayons in fichier_rayon:
            liste_rayons.append(ligne_rayons)
        for ligne_auteurs in fichier_auteurs:
            liste_auteurs.append(ligne_auteurs)
        for ligne_livres in fichier_livres:

            infos = ligne_livres.split(";")
            Titre = infos[1]
            auteur = infos[2]
            lanque = infos[3]
            categorie = infos[4]
            genre = infos[5]
            ref = infos[6]
            taille = infos[7]
            estDispo = infos[8]
            dateRetour = infos[9][:-1]

            if estDispo == 'True':
                estDispo = True
                dateRetour = None
            else:
                estDispo = False
                dateRetour = stringRetourToDateRetour(dateRetour)

            if infos[0] == 'False':
                mon_livre = Livre(Titre, auteur, lanque, genre, categorie, ref, taille,estDispo,dateRetour)
            else:
                dessinateur = infos[10]
                estEnCouleur = infos[11]
                if estEnCouleur == "True":
                    estEnCouleur = True
                else:
                    estEnCouleur = False
                mon_livre = BD(Titre, auteur, lanque, genre, categorie, ref, taille, dessinateur, estEnCouleur, estDispo, dateRetour)

            liste_livres.append(mon_livre)
            print(mon_livre.donneeImportante())
        for ligne_utilisateurs in fichier_utilisateurs:
            infos = ligne_utilisateurs.split(";")

            id = infos[1]
            lname = infos[2]
            fname = infos[3]
            mdp = infos[4]
            if infos[0] == 'False':
                mon_utilisateur = Personne(id, lname, fname, mdp)
            else:
                formule_user = infos[5]
                emprunts_user = infos[6]
                grade = stringGradeToDicoGrade(formule_user)
                if len(emprunts_user) > 5:
                    emprunts = stringEmpruntsToDicoEmprunts(emprunts_user)
                else:
                    emprunts = {}
                mon_utilisateur = User(id, lname, fname, mdp, grade)
                mon_utilisateur.initEmprunt(emprunts)
            liste_utilisateurs.append(mon_utilisateur)

        # ajout des listes dans les données de la bibliotheque
        une_bibliotheque.initialiserRayons(liste_rayons)
        une_bibliotheque.initialiserLivres(liste_livres)
        print(liste_livres)
        une_bibliotheque.initialiserAuteurs(liste_auteurs)
        une_bibliotheque.initialiserUtilisateurs(liste_utilisateurs)

        # fermeture des fichiers
        fichier_livres.close()
        fichier_utilisateurs.close()
        fichier_rayon.close()
        fichier_auteurs.close()

        # ajout de la bibliotheque complete dans la liste de bibliotheque
        liste_de_bibliotheque.append(une_bibliotheque)

    return liste_de_bibliotheque

"""
    Argument : liste_bibliothèque, list
    retour : None
    description : sauvegarde les données de chaque bibliotheque dans différents fichiers
"""
# sauvegarde les données de chaque bibliotheque dans différents fichiers
# attends un argument de type liste (liste de bibliotheques)
# ne retourne rien
def sauverDonnees(liste_bibliotheque):
    utils_deleteFile("liste_bibliotheque.txt")
    fichier_liste_biblio = open("liste_bibliotheque.txt", "a")
    for biblio in liste_bibliotheque:
        # ajoute le nom de la bibliotheque a la liste
        fichier_liste_biblio.write(f"{biblio.getNom()}\n")

        utils_deleteFile(f"biblio_{biblio.getNom()}_rayons.txt")
        utils_deleteFile(f"biblio_{biblio.getNom()}_auteurs.txt")
        utils_deleteFile(f"biblio_{biblio.getNom()}_livres.txt")
        utils_deleteFile(f"biblio_{biblio.getNom()}_utilisateurs.txt")

        # supprime les fichiers si ceux ci existent
        utils_deleteDoneeesBibliotheque(biblio.getNom())

        # ouverture des fichiers
        fichier_rayon = open(f"biblio_{biblio.getNom()}_rayons.txt", "a")
        fichier_auteurs = open(f"biblio_{biblio.getNom()}_auteurs.txt", "a")
        fichier_livres = open(f"biblio_{biblio.getNom()}_livres.txt", "a")
        fichier_utilisateurs = open(f"biblio_{biblio.getNom()}_utilisateurs.txt", "a")

        # obtention des listes de la bibliotheque
        les_rayons = biblio.getRayon()
        les_auteurs = biblio.getAuteur()
        les_livres = biblio.getListeLivre()
        les_utilisateurs = biblio.getUtilisateur()

        # écriture de chaque element dans le fichier qui correspond

        for un_rayon in les_rayons:
            fichier_rayon.write(f"{un_rayon}\n")
        for un_auteur in les_auteurs:
            fichier_auteurs.write(f"{un_auteur}\n")
        for un_livre in les_livres:
            fichier_livres.write(f"{un_livre.ligneDeDonnee()}\n")
        for un_utilisateur in les_utilisateurs:
            fichier_utilisateurs.writelines([f"{un_utilisateur.ligneDeDonnee()}\n"])

        # fermeture des fichiers
        fichier_rayon.close()
        fichier_auteurs.close()
        fichier_livres.close()
        fichier_utilisateurs.close()

        #NETOYAGE
        content = ""
        fichier_utilisateurs = open(f"biblio_{biblio.getNom()}_utilisateurs.txt", "r")
        for i in fichier_utilisateurs.read():
            content += i
        fichier_utilisateurs.close()
        fichier_utilisateurs = open(f"biblio_{biblio.getNom()}_utilisateurs.txt", "w")
        fichier_utilisateurs.write(content[:-1])
        fichier_utilisateurs.close()

        content = ""
        fichier_utilisateurs = open(f"biblio_{biblio.getNom()}_livres.txt", "r")
        for i in fichier_utilisateurs.read():
            content += i
        fichier_utilisateurs.close()
        fichier_utilisateurs = open(f"biblio_{biblio.getNom()}_livres.txt", "w")
        fichier_utilisateurs.write(content[:-1])
        fichier_utilisateurs.close()

        content = ""
        fichier_utilisateurs = open(f"biblio_{biblio.getNom()}_auteurs.txt", "r")
        for i in fichier_utilisateurs.read():
            content += i
        fichier_utilisateurs.close()
        fichier_utilisateurs = open(f"biblio_{biblio.getNom()}_auteurs.txt", "w")
        fichier_utilisateurs.write(content[:-1])
        fichier_utilisateurs.close()

        content = ""
        fichier_utilisateurs = open(f"biblio_{biblio.getNom()}_rayons.txt", "r")
        for i in fichier_utilisateurs.read():
            content += i
        fichier_utilisateurs.close()
        fichier_utilisateurs = open(f"biblio_{biblio.getNom()}_rayons.txt", "w")
        fichier_utilisateurs.write(content[:-1])
        fichier_utilisateurs.close()



    fichier_liste_biblio.close()

"""
    Argument : nom/prenom, string
    retour : bool
    description : Fonction qui vérifie la validité du nom et du prénom
"""
# Fonction qui vérifie la validité du nom et du prénom
# Attends un argument de type string (nom OU prénom)
# Retourne une booléen
def verifNom(nom):
    if len(nom) >= 3 and len(nom) <= 20:
        return True
    else:
        return False

"""
    Argument : password, string
    retour : bool
    description : Fonction qui vérifie la validité d'un mot de passe
"""
# fonction qui verifie la validité d'un mot de passe
# attends un argument de type string (le mot de passe)
# retourne un booléen
def motDePasseValable(password):
    au_moins_une_lettre_maj = False
    au_moins_une_lettre_min = False
    au_moins_un_chiffre = False
    au_moins_un_carac_special = False
    for i in range(len(password)):
        la_lettre = password[i]
        if estUneLettreCapitale(la_lettre):
            au_moins_une_lettre_maj = True
        elif estUneLettreMinuscule(la_lettre):
            au_moins_une_lettre_min = True
        elif estUnChiffre(la_lettre):
            au_moins_un_chiffre = True
        else:
            au_moins_un_carac_special = True
    if len(password) > 5 and au_moins_un_chiffre and au_moins_un_carac_special and au_moins_une_lettre_min and au_moins_une_lettre_maj:
        return True
    else:
        return False

def estUneLettreCapitale(letter):
    if ord(letter) >= 65 and ord(letter) <= 90:
        return True
    else:
        return False

def estUneLettreMinuscule(letter):
    if ord(letter) >= 97 and ord(letter) <= 122:
        return True
    else:
        return False

def estUnChiffre(letter):
    if ord(letter) >= 48 and ord(letter) <= 57:
        return True
    else:
        return False

"""
    Argument : (nom & prenom), string
    retour : string
    description :fonction générant un id utilisateur
"""
# fonction générant un id utilisateur
# attends deux arguments de type string
# retourne un string
def utils_genererId(nom, prenom):
    return f"{nom}.{prenom[0]}"


"""
    Argument : filename, string
    retour : None
    description :fonction spéciale supprimant un fichier
"""
# fonction spéciale supprimant un fichier
# attends un argument de type string (le nom de fichier)
# ne retourne rien
def utils_deleteFile(filename):
    if os.path.exists(filename):
        os.remove(filename)

"""
    Argument : Aucun
    retour : None
    description :Supprime toutes les données,  à n'utiliser QUE EN DEBUG **TRES RISQUÉ, pas de retour en arrière possible**
"""
# Supprime toutes les données
# à n'utiliser QUE EN DEBUG
# TRES RISQUÉ, pas de retour en arrière possible
# n'attend aucun argument
# ne retourne rien
def deleteAllDatas():
    file_list = os.listdir()
    for files in file_list:
        if files.endswith(".txt"):
            os.remove(files)



# Execute l'action d'un emprunt et l'enregistre

def emprunterUnLivre(utilisateurs, book):
    if utilisateurs.nombreEmpruntEnCours() > utilisateurs.getGrade()["Max Emprunts"]:
        print("Une erreur est survenue, vous avez dépassé votre nombre d'emprunts max")
    elif book.getTaille() > utilisateurs.getGrade()["Max Taille"]:
        print("Une erreur est survenue, vous n'avez pas une formule vous donnant accès à cet article")
    else:
        utilisateurs.ajouterEmprunt(book)
        date_retour = utilisateurs.getEmprunts()[book.getReference()]
        book.emprunter(date_retour)

def afficherFormules():
    Rules.voirGrades()


def selectionnerFormule(id):
    resultat = {}
    for i in Rules.liste_des_formules:
        if i["id"] == id:
            resultat = i
    if resultat == {}:
        print("Votre choix ne correspond à aucune formule, vous sera donc attribuée la formule 1")
        resultat = Rules.dico_grade_a
    return resultat

def closeProgramme():
    exit()


def devenirUtilisateur(liste_dutilisateurs, un_ancien_utilisateurs, un_nouvel_utilisateurs):
    for i in range(len(liste_dutilisateurs)):
        if liste_dutilisateurs[i] == un_ancien_utilisateurs:
            liste_dutilisateurs.pop(i)
    liste_dutilisateurs.append(un_nouvel_utilisateurs)


# fonction spéciale supprimant les fichiers d'une bibliotheque spécifiée
# attends un argument de type string (le nom d'une bibliotheque)
# ne retourne rien
def utils_deleteDoneeesBibliotheque(nom_bibliotheque):
    filename_rayons = f"biblio_{nom_bibliotheque}_rayons.txt"
    filename_auteurs = f"biblio_{nom_bibliotheque}_auteurs.txt"
    filename_livres = f"biblio_{nom_bibliotheque}_livres.txt"
    filename_utilisateurs = f"biblio_{nom_bibliotheque}_utilisateurs.txt"
    if os.path.exists(filename_rayons):
        os.remove(filename_rayons)
    if os.path.exists(filename_auteurs):
        os.remove(filename_auteurs)
    if os.path.exists(filename_livres):
        os.remove(filename_livres)
    if os.path.exists(filename_utilisateurs):
        os.remove(filename_utilisateurs)

def estEnLettre(str):
    for lettre in str:
        lettre_maj = lettre.upper()
        lettre_ascii = ord(lettre_maj)
        if lettre_ascii < 91 and lettre_ascii > 64:
            pass
        else:
            return False
    return True

def stringGradeToDicoGrade(le_string_grade):
    mon_futur_dico = {}
    spliter = le_string_grade.split(",")
    mon_futur_dico["id"] = int(spliter[0][-1])
    mon_futur_dico["Nom formule"] = spliter[1][-4:-1]
    mon_futur_dico["Max Emprunts"] = int(spliter[2][-1])
    mon_futur_dico["Max Taille"] = int(spliter[3][-2])
    return mon_futur_dico

def stringRetourToDateRetour(le_string_date):
    return datetime.date.fromisoformat(le_string_date)

def stringEmpruntsToDicoEmprunts(le_string_dico_emprunts):
    resultat = {}
    print(f"-----\n{le_string_dico_emprunts}\n--------")
    splitter = le_string_dico_emprunts[1:-1].split(",")
    nbr_info = int(len(splitter)/3)
    for i in range(nbr_info):
        a = splitter[(3 * i) + 0]
        annee = int(splitter[(3*i)+0][-4:])
        mois = int(splitter[(3*i)+1])
        jour = int(splitter[(3*i)+2][:-1])
        date_retour = datetime.date(annee, mois, jour)
        if a[0] == " ":
            .0
            a = a[1:]
        key = a[1:9]
        print(f"key {key}\tdate de retour : {date_retour}")
        print(key, date_retour)
        resultat[key] = date_retour
    return resultat


"""
    Argument : 
    retour : 
    description : 
    
    """
def creerRef(titre, auteur):
    number = random.randint(100001, 999999)
    resultat = f"{titre[0]}{auteur[0]}{number}"
    return resultat