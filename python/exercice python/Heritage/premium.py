import imp
from user import *
from banque import *


class Premium(User):
    
    def __init__(self, nom,mdp):
        super().__init__(nom,mdp)
        self.emprunt = 0

    def Emprunter(self,montant):
        self.emprunt += montant
        self.compte_bancaire.Crediter(montant)  
        self.banque = Banque()


    def __repr__(self):
        return self.nom







        # comment voir le nom de l'user premium
      



