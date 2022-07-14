import datetime

class ListCourses:
    # le constructeur
    def __init__(self, nom):
        self.nom = nom
        self.date_creation = str(datetime.date.today())
        self.a_acheter = []
        self.deja_achete = []

    # add est appelé lors d'un 'objet + item'
    def __add__(self, other):
        if not other in self:
            self.a_acheter.append(other)
            print("ajout de {} dans la liste {}".format(other, self.nom))
        else:
            print("{} est déja présent dans la liste".format(other))

    # sub est appelé lors d'un "objet - item"
    def __sub__(self, other):
        self.deja_achete.append(other)
        self.a_acheter.pop(self.a_acheter.index(other))
        print("{} de la liste {} acheté".format(other, self.nom))

    # getitem est appelé lors d'un 'objet[item]'
    def __getitem__(self, item):
        return self.a_acheter[item]

    # setitem est appelé lors d'un "objet[cle] = item"
    def __setitem__(self, key, value):
        self.a_acheter[key] = value

    # contains est appelé lors d'un "if item in objet"
    def __contains__(self, item):
        return item in self.a_acheter

    # iter est appelé lors d'une boucle for
    def __iter__(self):
        self.iterateur = 0
        return self


    def __next__(self):
        if self.iterateur < len(self.a_acheter):
            input()
            indice = self.iterateur
            self.iterateur += 1
            return self[indice]
        else:
            raise StopIteration

    # repr est appelé lors d'un print(objet)
    def __repr__(self):
        affiche = f"liste de {self.nom} à acheter faite le {self.date_creation}:\n"
        for i in self.a_acheter:
            affiche += "\t"+i+"\n"
        affiche += f"\nliste de {self.nom} deja acheté faite le {self.date_creation}:\n"
        for i in self.deja_achete:
            affiche += "\t"+i+"\n"
        return affiche

maListe = ListCourses("Nourriture")
# maListe + "banane"
maListe + "banane"
# maListe + "fraise"
# maListe + "lait"
# maListe + "oeuf"
# print(maListe)
# maListe - "banane"
# maListe - "fraise"
# print(maListe)
# print(maListe[0])
# maListe[1] = "huile"
# print(maListe)
# if "chocolat" in maListe:
#     print("le chocolat est déjà dans la liste")
# else:
#     maListe + "chocolat"

# for i in maListe:
#     print(i)