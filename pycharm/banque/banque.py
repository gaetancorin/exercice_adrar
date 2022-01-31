from prenium import Prenium
from user_banque import User


class Banque:

    def __init__(self):
        self.Nom = "BankCorin"
        self.pecule = 1000000
        self.liste_compteclient = []

    def Ajoutclientetcompte(self, compteclient):
        self.liste_compteclient.append(compteclient)
        if isinstance(compteclient, Prenium):
            print("Votre profil PRENIUM et compte en banque de Mr", compteclient.Nom, "a bien était enregistré à la banque", self.Nom)
        else:
            print("Votre profil USER et compte en banque de Mr", compteclient.Nom, "a bien était enregistré à la banque", self.Nom)

    def Emprunter(self, compteclient, somme):
        if somme >= self.pecule:
            print("Calmez Vous, vous aller faire tomber la Banque !")
        else:
            self.pecule -= somme
            print("Il reste", self.pecule, "€ à la BankCorin")
            compteclient.Dette(somme)
