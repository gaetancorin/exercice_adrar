def attribuerSection(age):
    sections = {"CP":6,"CE1":7,"CE2":8,"CM1":9,"CM2":10}
    #return list(sections.keys())[list(sections.values()).index(age)]
    for i in sections:
        if age == sections[i]:
            return i

def afficherEleves(effectifs):
    print("voici les élèves")
    for i in effectifs:
        print(i.nom,i.prenom,i.section)

class eleve:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self._section = attribuerSection(age)

    def Anniversaire(self):
        self.age += 1
        self._section = attribuerSection(self.age)

    def _ChangerSection(self, newSection):
        self._section = newSection

    def _getSection(self):
        return self._section

    def _delSection(self):
        del self._section
        
    def __repr__(self):
        return f"{self.prenom} {self.nom} est en {self.section}"

    section = property(_getSection, _ChangerSection, _delSection)