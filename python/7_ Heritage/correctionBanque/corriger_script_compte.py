from corriger_class_compte import Compte

nom = input("Quel est votre nom ?\n")
user = Compte(nom)

while True:
    choix = int(input("Que voulez vous faire ?\n\t"
                      "1: visualiser votre solde\n\t"
                      "2: créditer votre compte\n\t"
                      "3: débiter votre compte\n\t"
                      "4: Afficher vos les crédits éffectués\n"
                      "5: quitter"))
    if choix == 1:
        user.Afficher()
    elif choix == 2:
        montant = int(input("de combien souhaitez vous créditer ?\n"))
        user.Crediter(montant)
    elif choix == 3:
        mont= int(input("de combien souhaitez vous débiter ?\n"))
        user.Debiter(mont)
    elif choix == 4:
        user.AfficherCredits()
    else:
        print("Au revoir")
        break