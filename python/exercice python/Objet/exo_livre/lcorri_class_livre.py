class Livre():
    
    def __init__(self, auteur, titre,
                 genre):
        self.auteur = auteur
        self.titre = titre
        self.genre = genre
        self.nb_pages = 0
        self.pages = []

    def Ecrire(self, texte):
        self.pages.append(texte)
        self.nb_pages += 1

    def Effacer(self, num_page):
        self.pages.pop(num_page)
        self.nb_pages -= 1

    def AfficherPage(self, num_page):
        print(self.pages[num_page])

    def AfficherLivre(self):
        for i in self.pages:
            print("_____________", end="\n")
            print("|",i,sep="", end="|\n")
            print("_____________",end="\n")

    def Publier(self):
        print("Voici le nouveau livre de {} : {}. C'est une {} de {} pages.\nRégalez vous !"
              "".format(self.auteur,self.titre,self.genre,self.nb_pages))



monLivre = Livre("Lafon", "Demie vie", "Nouvelle")
monLivre.Ecrire("Lorem supli")
monLivre.Ecrire("Artud Lpois")
monLivre.Ecrire("Pheorte lui")
monLivre.AfficherLivre()
input()
monLivre.AfficherPage(2)
input()
monLivre.Publier()