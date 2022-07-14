# __add__ Pourquoi "not other in self" et pas "not other in self.deja_achete"?
# car il considère que cette éxécution est une itération self[0], self[1] etc. 
# Il va donc utilisé la méthode spécial __getitem__ qui retourne self.a_acheter[item]
# Mais si on enlève cette méthode, le programme ne fonctionne plus car une instance en elle même n'est pas itérable


class ListCourses:
    # le constructeur
    def __init__(self, nom):
        self.nom = nom
        self.a_acheter = []
        self.deja_achete = []

    # add est appelé lors d'un 'objet + item'
    def __add__(self, other):
        if not other in self:
            self.a_acheter.append(other)
            print("pas dedans")
        elif "Nourriture" in self.nom:
            print("passe")
        else:
            print("dedans")

    # getitem est appelé lors d'un 'objet[item]'
    def __getitem__(self, item):
        return self.a_acheter[item]

maListe = ListCourses("Nourriture")
maListe + "banane"
maListe + "banane"
