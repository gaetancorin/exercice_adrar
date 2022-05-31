from user_banque import User


class Prenium(User):

    def __init__(self, Nom, Mdp):
        super().__init__(Nom, Mdp)
        self.Emprunt = 0

    def Dette(self, montant):
            self.CompteBancaire.Afficher()
            self.Emprunt += montant
            print("Vous venez d'emprunter", montant, "euros")
            print("Vous avez une Dette de", self.Emprunt, "euros")
            self.CompteBancaire.Crediter(montant)

# gaetan = Prenium("corin", "coco")
# gaetan.afficherInformations()
# gaetan.CreerCompte(50)
# gaetan.afficherInformations()
# gaetan.Emprunter(10)
