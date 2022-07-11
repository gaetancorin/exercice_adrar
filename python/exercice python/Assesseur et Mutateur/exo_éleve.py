import re 

class Eleve():
    
    def __init__(self, nom , prenom , age):
       self.nom = nom
       self;prenom = prenom
       self.age = age
       self._section = ''
    
    def _Section(self):
        dico = {"petite-section": 4, "moyenne-section": 5, "grande-section": 5, "CP": 7,"CE1" : 8, "CE2" : 9, "CM1" : 10, "CM2": 11}
        for i in dico:
            if self.age < dico[i]:
                self._section = i       
     