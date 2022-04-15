from Livre import Livre


class BD(Livre):

    def __init__(self, titre, auteur, langue, genre, categorie, couleur, dessinateur, ref="", dispo=True, retour=None):
        super().__init__(titre, auteur, langue, genre, categorie, ref, dispo, retour)
        self.couleur = couleur
        self.dessinateur = dessinateur

    def __repr__(self):
        return str(f"{self.titre} ; {self.auteur} ; {self.langue} ; {self.genre} ; {self.categorie} ; {self.ref} ; {self.dispo} ; {self.retour} ; {self.couleur} ; {self.dessinateur}")

# b = BD("Injustice 1", "DC", "Français", "Fantastique", "BD", "ID104382", "True", "None", "True", "J Raapack")
# print(b)
