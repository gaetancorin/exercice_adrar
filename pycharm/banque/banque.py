from prenium import Prenium
from user_banque import User

class Banque:

    def __init__(self):
        self.Nom = "BankCorin"
        self.pecule = 1000000
        self.liste_compteclient = []

    def Ajoutclientetcompte(self, compte):
        self.liste_compteclient.append(compte)
        if isinstance(compte, Prenium):
            print("Le compte Prenium et compte en banque de Mr", compte.Nom, "a bien était enregistré à la banque", self.Nom)
        if isinstance(compte, User) and not isinstance(compte, Prenium):
            print("Le compte User et compte en banque de Mr", compte.Nom, "a bien était enregistré à la banque", self.Nom)

    def Emprunter(self, compteclient, somme):
        if somme >= self.pecule:
            print("Calmez Vous, vous aller faire tomber la Banque !")
        else:
            self.pecule -= somme
            print("Il reste", self.pecule, "€ à la BankCorin")
            for i in self.liste_compteclient:
                if i == compteclient:
                    i.Dette(somme)

