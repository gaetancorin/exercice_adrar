from user_banque import User


class Prenium(User):

    def __init__(self, Nom, Mdp):
        super().__init__(Nom, Mdp)
        self.Emprunt = 0

    def Emprunter(self, montant):
        if self.CompteBancaire == 0:
            print("Vous ne pouvez pas emprunter tant que vous n'avez pas de compte bancaire")
        else:
            self.CompteBancaire.Afficher()
            self.Emprunt += montant
            print("Vous venez d'emprunter", montant, "euros")
            print("Votre emprunt total est de", self.Emprunt, "euros")
            self.CompteBancaire.Crediter(montant)

# gaetan = Prenium("corin", "coco")
# gaetan.afficherInformations()
# gaetan.CreerCompte(50)
# gaetan.afficherInformations()
# gaetan.Emprunter(10)
