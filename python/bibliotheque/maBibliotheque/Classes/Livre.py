from random import randrange


class Livre:

    def __init__(self, titre, auteur, langue, genre, categorie, ref, dispo, retour):
        self.titre = titre
        self.auteur = auteur
        self.langue = langue
        self.genre = genre
        self.categorie = categorie
        self.ref = ref
        self.dispo = dispo
        self.retour = retour

    def definirRef(self):
        self.ref = str(self.titre[0] + self.auteur[0] + str(randrange(0, 999999)))

    def __repr__(self):
        return str(f"{self.titre} ; {self.auteur} ; {self.langue} ; {self.genre} ; {self.categorie} ; {self.ref} ; {self.dispo} ; {self.retour}")

# a = Livre("Harry Potter 1", "J.K Rowling", "Français", "Fantastique", "Roman", "HJ135203", "True", "None")
#
# print(a)
