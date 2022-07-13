from user import *


class Premium(User):
    
    def __init__(self, nom,mdp):
        super().__init__(nom,mdp)
        self.emprunt = 0

    def Emprunter(self,montant):
        self.compte_bancaire.Crediter(montant)   

    def __repr__(self):
        return self.nom







        # comment voir le nom de l'user premium
      



