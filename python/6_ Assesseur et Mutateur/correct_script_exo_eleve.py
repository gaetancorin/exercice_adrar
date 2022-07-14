import lesEleves

effectif = []

while True:

    #Affichage des élèves
    if effectif:
        lesEleves.afficherEleves(effectif)

    #Définition du type d'utilisateur
    user = input("Etes vous secretaire ou professeur ? (1/2)\n")

    #Utilisateur secrétaire
    if user == "1":
        choix = input("souhaitez vous ajouter un eleve ou déclarer un anniverasaire ? (1/2)\n")

        #Ajout d'un nouvel élève dans la liste d'éffectifs
        if choix == "1":
            #premiere syntaxe
            effectif.append(lesEleves.eleve(input("indiquez le nom\n"), input("prenom\n"), int(input("age\n"))))

            #deuxieme syntaxe
            nom = input("nom ?")
            prenom = input("prenom ?")
            age = input("age ?")
            monEleve = lesEleves.eleve(nom, prenom, age)
            effectif.append(monEleve)

            #troisieme syntaxe
            nom = input("nom ?")
            prenom = input("prenom ?")
            age = input("age ?")
            effectif.append(lesEleves.eleve(nom, prenom, age))

        #Anniversaire d'un élève
        elif choix == "2":
            lesEleves.afficherEleves(effectif)

            nom = input("indiquez le nom de l'élève qui fête son anniversaire\n")

            #Comparaison de l'attribut nom de chaque case de la liste avec le nom input
            for i in effectif:
                if i.nom == nom:
                    #Appel de la fonction Anniversaire de l'objet i
                    i.Anniversaire()

        else:
            print("Entrée incorrecte, redémarrage du programme")

    #Utilisateur professeur
    elif user == "2":
        lesEleves.afficherEleves(effectif)

        nom = input("indiquez le nom de l'élève qui doit changer de section")
        newSection = input("indiquez le nom de sa nouvelle section")
        #Comparaison de l'attribut nom de chaque case de la liste avec le nom input
        for i in effectif:
            if i.nom == nom:
                #Utilisation du setter _ChangerSection par la property section
                i.section = newSection
    elif user == "quit":
        break
    else:
        print("Entrée incorrecte, redémarrage du programme")