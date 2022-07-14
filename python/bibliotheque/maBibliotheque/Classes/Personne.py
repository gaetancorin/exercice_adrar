class Personne:

    def __init__(self, id,  nom, prenom, mdp):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.mdp = mdp

    def __repr__(self):
        return str(f"{self.nom},{self.prenom},{self.mdp}")

    def definirID(self):
        self.id = str(self.nom[0]+"."+self.prenom)

    def changerMotDePasse(self, motdepasse):
        self.mdp = motdepasse






# c = Personne("p.maxime", "przybylo", "maxime", "Azerty77")
# print(c.nom)
# print(c.Id)
# c.DefinirID()
# print(c.Id)
