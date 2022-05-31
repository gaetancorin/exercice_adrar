import datetime

class Compte:

    def __init__(self, proprio):
        self.date_creation = str(datetime.date.today())
        self.solde = 0
        self.proprietaire = proprio
        self.banque = "BankCorin"

    def Crediter(self, montant):
        self.solde += montant
        print("Votre compte a bien été crédité de {}€".format(montant))
        self.Afficher()

    def Debiter(self, montant):
        if self.solde >= montant:
            self.solde -= montant
            print("Votre compte a bien été débité de {}€".format(montant))
            self.Afficher()
        else:
            print("erreur, vous n'avez pas assez d'argent")

    def Afficher(self):
        print("Vous disposez de {}€ sur votre compte".format(self.solde))

# gaetan = Compte("gaetan")
# gaetan.Crediter(100)
# gaetan.Debiter(50)
# gaetan.Afficher()
