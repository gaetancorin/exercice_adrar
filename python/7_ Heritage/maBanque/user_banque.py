from compte import Compte

class User:

    def __init__(self, Nom, Mdp):
        self.Nom = Nom
        self.Mdp = Mdp
        self.CompteBancaire = 0

    def afficherInformations(self):
        if self.CompteBancaire != 0:
            print("Votre Nom est", self.Nom, ", votre mot de passe est", self.Mdp, ", votre montant du compte bancaire est de ", self.CompteBancaire.solde, "euros")
        else:
            print("Votre Nom est", self.Nom, ", votre mot de passe est", self.Mdp, ", vous n'avez pas encore de compte bancaire")

    def CreerCompte(self, Montant):
        self.CompteBancaire = Compte(self.Nom)
        self.CompteBancaire.Crediter(Montant)


# gaetan = User("corin", "1234")
# gaetan.CreerCompte(10)
# gaetan.afficherInformations()










