from fonction_enregistrement import adresse_email, categorie_age
from enregistrement_csv import ecrire, lire
from datetime import date

# demander si connaissance du nombre de personne a inscrire et la quantité de personnes
while True:
    connaitre_nombre = input("Connaissez-vous le nombres de personnes a inscrire? Oui(1) / Non(2)\n")
    if connaitre_nombre == "1" or connaitre_nombre == "2":
        break
    else:
        print("Merci de répondre par le chiffre 1 ou le chiffre 2")

if connaitre_nombre == "1":
    while True:
        try:
            nbr_a_inscrire = int(input("Combien de demande d'inscription souhaitez vous faire?\n"))
            break
        except ValueError:
            print("Ce n'est pas un nombre valide, entrez un nombre sous forme de chiffres")
if connaitre_nombre == "2":
    nbr_a_inscrire = 0

# liste qui enregistre tous les enregistrements
liste_final =[]

# réaliser l'enregistrement si nombre de personnes connu
if nbr_a_inscrire >= 1:
    for i in range(1, nbr_a_inscrire + 1):
        print("-------", i, "inscription ------")
        nom = input("insérer le nom\n")
        prenom = input("insérer le prénom\n")

        while True:
            try:
                annee = int(input("insérer l'année de naissance\n"))
            except ValueError:
                print("Ce n'est pas un nombre valide, entrez un nombre sous forme de chiffres")
            if annee >= 1900 and annee < 2050:
                break
            else:
                print("entrez une date de naissance à partir de 1900.")

        email = adresse_email(nom, prenom)
        categorie = categorie_age(annee)

        enregistrement = [nom,prenom,email,categorie]
        print(enregistrement)
        liste_final.append(enregistrement)


# réaliser l'enregistrement si nombre de personnes inconnus
if nbr_a_inscrire == 0:
    while True:
        while True:
            ajout_nv_personne = input("Voulez vous ajouter un nouvel enregistrement? Oui(1) / Non(2)\n")
            if ajout_nv_personne == "1" or ajout_nv_personne == "2":
                break
            else:
                print("Merci de répondre par le chiffre 1 ou le chiffre 2")

        if ajout_nv_personne == "1":
            nbr_a_inscrire += 1
            print("-------", nbr_a_inscrire, "inscription ------")
            nom = input("insérer le nom\n")
            prenom = input("insérer le prénom\n")

            while True:
                try:
                    annee = int(input("insérer l'année de naissance\n"))
                except ValueError:
                    print("Ce n'est pas un nombre valide, entrez un nombre sous forme de chiffres")
                if annee >= 1900 and annee < 2050:
                    break
                else:
                    print("entrez une date de naissance à partir de 1900.")

            email = adresse_email(nom, prenom)
            categorie = categorie_age(annee)

            enregistrement = [nom, prenom, email, categorie]
            print(enregistrement)
            liste_final.append(enregistrement)

        if ajout_nv_personne == "2":
            break

print("LA LISTE DE TOUT LES INSCRITS",liste_final)



date_du_jour = str(date.today())
ecrire("inscrits-"+ date_du_jour+".csv", liste_final)
lire("inscrits-"+ date_du_jour+".csv")





