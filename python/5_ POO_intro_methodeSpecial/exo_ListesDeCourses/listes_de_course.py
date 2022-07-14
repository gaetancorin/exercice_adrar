from datetime import date

class Course:
    
    def __init__(self, nom):
        self.nom = nom
        self.date_creation = str(date.today())
        self.besoin = []
        self.dispo =[]
        
    def __add__(self, item):
        if not item in self:
            self.besoin.append(item)
            print(f"Ajout de {item} dans la liste {self.nom}")
        
    def __sub__(self, item):
        self.dispo.append(item)
        self.besoin.pop(self.besoin.index(item))
        
        
    def __contains__(self, item) :
        return item in self.dispo
    
    def __getitem__(self, item):
        return self.besoin[item]
    
    def __setitem__(self, cle, item):
        self.besoin[cle] = item
    
    def __iter__(self):
        self.n = 0 
        return self
    
    def __next__(self):
        if self.n < len(self.besoin) :
            indice = self.n
            self.n += 1
            return self.besoin[indice]
        else :
            raise StopIteration
        
    def __repr__ (self):
        affiche = f"voici la listes des courses {self.nom}\n"
        for i in self.besoin:
            affiche += i+"\n"
        return affiche            
            
