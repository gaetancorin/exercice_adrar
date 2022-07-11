class Compte:
    banque = 'cannappin'
    
    def __init__ (self, date_creation, solde, proprio) :
        self.date_creation = date_creation
        self.solde = solde
        self.proprio = proprio
        
    
    def Crediter(self,montant):
        self.solde + montant 
        self.montant = montant
        print(self.solde)
        
    def Debiter(self, montant):
        self.solde - montant
        self.montant = montant 
        print(self.solde)
    
    def Afficher(self, solde, date_creation,  proprio ):
        print(solde, date_creation, proprio )
        self.date_creation = date_creation
        self.solde = solde
        self.proprio = proprio