from corriger_class_compte import * 


class User:
    
    def __init__(self,nom, mdp) :
        self.nom = nom
        self.mdp = mdp
       

    def CreerCompte(self,depot):
        self.compte_bancaire = Compte(self.nom)
        self.compte_bancaire.Crediter(depot)

    def Affichercompte(self):
        self.compte_bancaire.Afficher()

    def __repr__(self):
        return self.nom
        
           
    

# mon_user = User('gokool','azerty')
# mon_user.CreerCompte(100)
# mon_user.Affichercompte()